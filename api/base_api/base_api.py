
import allure
import json
from dotenv import load_dotenv
from typing import List
from playwright.sync_api import APIRequestContext, expect
from api.utils.logger import get_logger
from http import HTTPStatus

load_dotenv()

class BaseApi:

    def __init__(self, request_context: APIRequestContext):
        self.request = request_context
        self.response = None
        self.logger = get_logger(self.__class__.__name__)

    @allure.step(f"Check status code")
    def check_response_status_code(self, status_code: HTTPStatus):
        self.logger.info(f"Check status code: {status_code}")
        assert self.response.status == status_code

        allure.attach(
            f"Expected: {status_code}\n",
            f"Actual: {self.response.status}\n\"",
            f"URL: {self.response.url}\n",
            attachment_type=allure.attachment_type.TEXT
        )
        return self

    @allure.step("Validate response model")
    def check_model(self, model_class):
        self.logger.info(f"Validate response model: {model_class.__name__}")
        self.model = model_class(**self.response.json())

        allure.attach(
            json.dumps(self.model.dict(), indent=2, ensure_ascii=False),
            name="Response model",
            attachment_type=allure.attachment_type.JSON
        )

        return self

    @staticmethod
    def field_data(value, data):
        if isinstance(data, str):
            if value != data:
                raise ValueError(f"Поле не содержит {value}, а содержит {data}")
        elif isinstance(data, List):
            if value != data:
                raise ValueError(f"Поле не содержит {value}, а содержит {data}")
        else:
            raise TypeError(f"Неподдерживаемый тип: {type(value)}")
