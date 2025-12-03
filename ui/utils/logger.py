
import logging
import os
from datetime import datetime
from playwright.sync_api import Page

def setup_logger() -> logging.Logger:

    log_dir = "logs" # папка для логов, если ее нет
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger("ui_tests")
    logger.setLevel(logging.INFO) # уровень __name__
    logger.handlers.clear()

    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    log_file = f"{log_dir}/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(log_format))

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(log_format))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info(f"Logger initialized: {log_file}")

    return logger

logger = setup_logger()



class PlaywrightLogger:
    def __init__(self, page: Page):
        self.page = page
        self.request_count = 0
        self.error_count = 0

    def setup(self, parent_logger_name: str = "ui_tests"):
        self.logger = logging.getLogger(f"{parent_logger_name}.playwright")

        self.page.on("console", self._handle_console) # перехват console.log из браузера
        self.page.on("pageerror", self._handle_page_error) # перехват ошибок страницы
        self.page.on("dialog", self._handle_dialog) # перехват диалогов (alert, confirm, prompt)
        self.page.on("request", self._handle_request) # перехват запросов
        self.page.on("response", self._handle_response)  # перехват ответов

        self.logger.info("Playwright logger initialized")

    def _handle_console(self, msg): # обработка сообщений браузера
        level = msg.type
        text = msg.text
        location = msg.location

        level_map = {
            'log': logging.INFO,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'debug': logging.DEBUG
        }

        log_level = level_map.get(level, logging.INFO)

        log_msg = f"Browser console [{level}]: {text}"


        if level == 'error':
            location = msg.location
            if location:
                log_msg = f"❌ Browser console error: {text} at {location.get('url')}:{location.get('lineNumber')}"
            else:
                log_msg = f"❌ Browser console error: {text}"
            self.error_count += 1
        else:
            log_msg = f"Browser console {level}: {text}"

        self.logger.log(log_level, log_msg)


    def _handle_page_error(self, error):
        self.error_count += 1
        self.logger.error(f"❌ JavaScript error: {error}")

    def _handle_dialog(self, dialog):
        dialog_type = dialog.type
        message = dialog.message
        self.logger.warning(f"💬 Browser {dialog_type} dialog: {message}")

        try:
            dialog.accept()
            self.logger.info(f"✅ Dialog accepted: {message}")
        except Exception as e:
            self.logger.error(f"❌ Failed to gandle dialog: {e}")

    def _handle_request(self, request):
        self.request_count += 1
        self.logger.debug(f"📤 Request #{self.request_count}: {request.method} {request.url}")

    def _handle_response(self, response):
        if response.status >= 400:
            self.error_count += 1
            try:
                body = response.text()
                self.logger.warning(f"⚠️ Response {response.status} for {response.url}: {body[:200]}...")
            except:
                self.logger.warning(f"⚠️ Response {response.status}: {response.url}")

    def get_stats(self):
        return {
            "requests": self.request_count,
            "errors": self.error_count,
            "timestamp": datetime.now().isoformat()
        }

    def log_screenshot(self, description: str = "Screenshot"):
        try:
            screenshot_path = f"logs/screenshot_{datetime.now().strftime('%H%M%S')}.png"
            self.page.screenshot(path=screenshot_path, full_page=True)
            self.logger.info(f"📸 {description} saved to {screenshot_path}")
        except Exception as e:
            self.logger.error(f"❌ Failed to take screenshot: {e}")