import os
import imaplib
import email
import time
from email.policy import default
from dotenv import load_dotenv
import re

load_dotenv()

IMAP_SERVER = f"{os.getenv('IMAP_SERVER')}"
IMAP_PORT = int(f"{os.getenv('IMAP_PORT')}")
IMAP_EMAIL_ACCOUNT = f"{os.getenv('IMAP_MAIL_USER')}"
IMAP_PASSWORD = f"{os.getenv('IMAP_PASSWORD')}"

class GetConfirmCode:

    @staticmethod
    def get_confirm_code_from_latest_email():
        """
        Парсим код из тела письма
        :return:
        """
        print(f"\n Пауза 20 сек")
        time.sleep(20)
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        status_server, response_server = mail.login(IMAP_EMAIL_ACCOUNT, IMAP_PASSWORD)
        print(f"Status login: {status_server} {response_server}")
        mail.select('INBOX')
        status_mail, messages = mail.search(None, 'ALL')
        print(f"Status mail: {status_mail}")
        if status_mail != 'OK' or not messages[0]: #id messages
            return None, "В ящике нет писем"
        email_ids = messages[0].split() # список id писем
        latest_email_id = email_ids[-1] # выбираем последнее письмо
        status_email, data = mail.fetch(latest_email_id, '(RFC822)')
        if status_email != 'OK':
            return None, f"Ошибка получения письма с ID {latest_email_id}"
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email, policy=default)
        #subject, encoding = decode_header(msg["Subject"])[0] if msg["Subject"] else ("Без темы", None)
        email_body = msg.get_payload(decode=True).decode() # тело письма
        #print(email_body)
        five_digit_pattern = r'\b(\d{5})\b'
        match = re.search(five_digit_pattern, email_body)
        if match:
            confirm_code = match.group(1)
        print(f"\n ******************** \n Confirm code: {confirm_code} \n ********************")
        mail.close()
        mail.logout()
        return confirm_code

#GetConfirmCode.get_confirm_code_from_latest_email()