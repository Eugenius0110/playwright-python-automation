
import time
from playwright.sync_api import Page, expect, Locator
#from playwright.async_api import Page, expect, Locator


class BasePage:

    url = None
    def __init__(self, page: Page):
        self.page = page

    def get_element(self, element_dict: dict) -> Locator:
        if element_dict.get("role") and element_dict.get("text"):
            element = self.page.getget_by_role(element_dict.get("role"), name=element_dict.get("text"))
        else:
            element = self.page.locator(element_dict.get('selector'))

        return element

        #if element_dict.get('data-testid'):
        #     element = self.page.get_by_test_id(element_dict.get('data-testid'))
        # else:
        #     element = self.page.locator(element_dict.get('selector'))


    def element_click(self, element_dict: dict):
        element = self.get_element(element_dict)
        element.click()

    def check_element_attached(self, element_dict: dict): # проверяем, что элемент прикреплен к DOM
        element = self.get_element(element_dict)
        expect(element).to_be_attached()
        print(f"✅ Element attached DOM: {element_dict.get('description')}")

    def check_element_visible(self, element_dict: dict): # проверяем, что элемент видим
        element = self.get_element(element_dict)
        expect(element).to_be_visible()
        print(f"✅ Element visible: {element_dict.get('description')}")

    def check_element_enabled(self, element_dict: dict): # проверяем, что элемент доступен
        element = self.get_element(element_dict)
        expect(element).to_be_enabled()
        print(f"✅ Element enabled: {element_dict.get('description')}")

    def check_element_has_text(self, element_dict: dict): # проверяем, что элемент содержит текст
        element = self.get_element(element_dict)
        expect(element).to_have_text(element_dict.get('text'))
        print(f"✅ Element {element_dict.get('description')} has text: {element_dict.get('text')}")

    def check_element_editable(self, element_dict: dict): # проверяем, что элемент редактируемый
        element = self.get_element(element_dict)
        expect(element).to_be_editable()
        print(f"✅ Element editable:{element_dict.get('description')}")

    def check_element_focus(self, element_dict: dict):  # проверяем, что элемент в фокусе
        element = self.get_element(element_dict)
        element.focus()
        expect(element).to_be_focused()
        print(f"✅ Element in focus: {element_dict.get('description')}")

    def check_element_click(self, element_dict: dict): # проверяем, что на элемент можно кликнуть
        element = self.get_element(element_dict)
        element.click()
        print(f"✅ Element clickable: {element_dict.get('description')}")

