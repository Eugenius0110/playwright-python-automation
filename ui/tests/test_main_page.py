
import sys
import os
from time import sleep

import pytest
from playwright.sync_api import Page
from pathlib import Path
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright

# current_dir = Path(__file__).parent
# frontend_root = current_dir.parent
# sys.path.insert(0, str(frontend_root))
# from pages.simple_page import SimplePage

from ui.pages.main_page import MainPage
from ui.pages.elements.selectors import MainPageSelectors



# @pytest.mark.ui
# @pytest.mark.smoke
# @pytest.mark.parametrize('element_dict',
#                          [MainPageSelectors.button_enter]
#                          )
def test_button_enter_exists(main_page: MainPage):
    main_page.check_element_attached(MainPageSelectors.button_enter)
    main_page.check_element_visible(MainPageSelectors.button_enter)
    main_page.check_element_enabled(MainPageSelectors.button_enter)
    main_page.check_element_has_text(MainPageSelectors.button_enter)
    main_page.check_element_focus(MainPageSelectors.button_enter)
    main_page.get_element(MainPageSelectors.button_enter).click()

def test_button_favorite(main_page: MainPage):
    main_page.check_element_attached(MainPageSelectors.button_logo)
    main_page.check_element_visible(MainPageSelectors.button_logo)
    main_page.check_element_enabled(MainPageSelectors.button_logo)
    main_page.check_element_focus(MainPageSelectors.button_logo)
    main_page.check_element_click(MainPageSelectors.button_logo)


