
import os
import json
from faker import Faker
from dotenv import load_dotenv
from api.yandex_mail_api.get_code_from_email import GetConfirmCode

load_dotenv()
fake = Faker()


class SignUpPayload:

    phone = "+79781234567"
    phone_2 = "+79781234112"

    payload_signup_ok = {
        "firstName": f"{fake.first_name()}-autotest",
        "lastName": f"{fake.last_name()}-autotest",
        "phoneNumber": f"{phone}",
        "email": f"{os.getenv('TEST_EMAIL_USER')}"
    }

    # payload_signup_already_phone_reg = {
    #     "last_name": f"{fake.last_name()}-autotest",
    #     "first_name": f"{fake.first_name()}",
    #     "phone": f"{phone}",
    #     "email": f"{os.getenv('TEST_EMAIL_USER_2')}"
    # }
    #
    # payload_signup_already_email_reg = {
    #     "last_name": f"{fake.last_name()}-autotest",
    #     "first_name": f"{fake.first_name()}",
    #     "phone": f"{phone_2}",
    #     "email": f"{os.getenv('TEST_EMAIL_USER')}"
    # }

class LoginPayload:

    payload_user_admin_login_success = {
        "phoneNumberOrEmail": f"{os.getenv('ADMIN_EMAIL')}",
        "password": f"{os.getenv('ADMIN_PASSWORD')}"
    }

    payload_create_suser_login_success = {
        "email": f"{os.getenv('TEST_EMAIL_USER')}",
        "password": f"{os.getenv('TEST_PASSWORD')}"
    }

    payload_email_not_exist = {
        "email": f"{os.getenv('TEST_EMAIL_USER_2')}",
        "password": f"{os.getenv('TEST_PASSWORD')}"
    }

    payload_password_incorrect = {
        "email": f"{os.getenv('TEST_EMAIL_USER_2')}",
        "password": f"{os.getenv('TEST_PASSWORD')}incorrect"
    }

    payload_email_empty = {
        "email": f"",
        "password": f"{os.getenv('TEST_PASSWORD')}"
    }


class ConfirmCodePayload:

    payload_confirm_code_invalid = {
        "email": f"{os.getenv('TEST_EMAIL_USER')}",
        "confirmation_code": "00000"
    }

    @staticmethod
    def get_confirm_code():
        get_confirm_code = GetConfirmCode.get_confirm_code_from_latest_email()
        payload_confirm_code = {
            "email": f"{os.getenv('TEST_EMAIL_USER')}",
            "confirmation_code": f"{get_confirm_code}"
        }
        return payload_confirm_code


class SetPasswordPayload():


    payload_password_match = {
        "email": f"{os.getenv('TEST_EMAIL_USER')}",
        "password": f"{os.getenv('TEST_PASSWORD')}",
        "password_confirm": f"{os.getenv('TEST_PASSWORD')}"
    }

    payload_password_not_match = {
        "email": f"{os.getenv('TEST_EMAIL_USER')}",
        "password": f"{os.getenv('PASSWORD')}",
        "password_confirm": f"{os.getenv('TEST_PASSWORD')}0"
    }

    email_not_exist = "eug0123@yadex.ru"
    payload_user_not_exist_400 = {
        "email": f"{email_not_exist}",
        "password": f"{os.getenv('TEST_PASSWORD')}",
        "password_confirm": f"{os.getenv('TEST_PASSWORD')}"

    }

    password_short_7 = fake.password(length=7)
    payload_password_short = {
        "email": f"{os.getenv('TEST_EMAIL_USER')}",
        "password": f"{password_short_7}",
        "password_confirm": f"{password_short_7}"
    }

    password_long_257 = fake.password(length=257)  # 256 character
    payload_password_long = {
        "email": f"{os.getenv('TEST_EMAIL_USER')}",
        "password": f"{password_long_257}",
        "password_confirm": f"{password_long_257}"
    }


    payload_password_with_space = {
        "email": f"{os.getenv('TEST_EMAIL_USER')}",
        "password": f"{os.getenv('TEST_PASSWORD')} s",
        "password_confirm": f"{os.getenv('TEST_PASSWORD')} s"
    }

    password_invalid_characters = "1234567aテスト"
    payload_password_invalid_characters = {
        "email": f"{os.getenv('TEST_EMAIL_USER')}",
        "password": f"{password_invalid_characters}",
        "password_confirm": f"{password_invalid_characters}"
    }
