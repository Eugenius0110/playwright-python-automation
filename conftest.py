

import pytest
import allure
from playwright.sync_api import Playwright, APIRequestContext
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope='session')
@allure.title("Prepare API context")
def api_request_context(playwright: Playwright):
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()
