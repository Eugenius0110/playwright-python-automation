import time

import pytest
import os
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
from ui.pages.base_page import BasePage


load_dotenv()

BASE_URL = f"{os.getenv('BASE_URL_1')}"


class MainPage(BasePage):
    url = BASE_URL

    def open(self):
        self.page.goto(self.url)



