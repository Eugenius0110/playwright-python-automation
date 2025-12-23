import allure
import json
import pydantic
from dotenv import load_dotenv
from typing import List
from playwright.sync_api import APIRequestContext
from api.utils.logger import get_logger
from http import HTTPStatus

load_dotenv()


class BaseApi:

    def __init__(self, request_context: APIRequestContext):
        self.request = request_context
        self.response = None
        self.logger = get_logger(self.__class__.__name__)

    @allure.step("Check status code")
    def check_response_status_code(self, status_code: HTTPStatus):
        self.logger.info(f"Check status code: {status_code}")
        if self.response.status == status_code:
            self.logger.info(f"✅ Status code is valid: {self.response.status}")
            allure.attach(
                body=f"Expected: {status_code}\nActual: {self.response.status}\n\"URL: {self.response.url}\n",
                name="Status code validation",
                attachment_type=allure.attachment_type.TEXT
            )
            return self
        else:
            self.logger.error(f"❌ Status code is invalid: expected {status_code}, got {self.response.status}")
            allure.attach(
                body=f"URL: {self.response.url}\nExpected: {status_code}\nActual: {self.response.status}",
                name="Status code validation",
                attachment_type=allure.attachment_type.TEXT
            )
            raise AssertionError(f"❌ Expected status code is invalid: {status_code}, got {self.response.status}")

    @allure.step("Validate response model")
    def check_model(self, model_class):
        self.logger.info(f"Validate response model: {model_class.__name__}")
        response_json = self.response.json()
        #self.logger.debug(f"Response raw: {json.dumps(response_json, indent=4, ensure_ascii=False)}")
        try:
            self.model = model_class(**response_json)
            self.logger.info(f"✅ Response model is valid")
            allure.attach(
                body=json.dumps(response_json, indent=4, ensure_ascii=False), # self.model.model_dump()
                name="Response model",
                attachment_type=allure.attachment_type.TEXT
            )
        except Exception as e:
            self.logger.error(f"❌ Model validation failed: {e}")
            raise AssertionError(f"❌ Model validation failed: {e}")
        return model_class(**response_json)

    @staticmethod
    def check_field_data(actual, expected):
        if isinstance(actual, str):
            if actual != expected:
                raise ValueError(f'❌ Поле не содержит "{expected}", а содержит "{actual}"')
        elif isinstance(actual, List):
            if actual != expected:
                raise ValueError(f'❌ Поле не содержит "{expected}", а содержит "{actual}"')
        else:
            raise TypeError(f"❌ Неподдерживаемый тип: {type(actual)}")
