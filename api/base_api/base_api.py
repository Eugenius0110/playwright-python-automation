
import os
import pytest
from dotenv import load_dotenv
from typing import List
from playwright.sync_api import APIRequestContext, expect, Playwright
from http import HTTPStatus

load_dotenv()

class BaseApi:
    BASE_URL = f"{os.getenv('HOST_TEAM_2')}"
    TEST_EMAIL_USER = f"{os.getenv('TEST_EMAIL_USER')}."

    def __init__(self, request_context: APIRequestContext):
        #self.request =
        self.response = None
        self.model = None

    def print_response(self):
        print(f"\n{self.response.json()}")

    def check_response_status_code(self, status_code: HTTPStatus):
        assert self.response.status_code == status_code, f"Ожидался {status_code}, пришел {self.response.status_code}\n{self.response.json()}"
        return self.response.status_code

    def check_model(self, model_class):
        self.model = model_class(**self.response.json())
        return self.model

    @staticmethod
    def field_data(value, data):
        if isinstance(data, str):
            if value != data:
                raise ValueError(f"Поле не содержит {data}, а содержит {value}")
        elif isinstance(data, List):
            if value != data:
                raise ValueError(f"Поле не содержит {data}, а содержит {value}")
        else:
            raise TypeError(f"Неподдерживаемый тип: {type(value)}")
