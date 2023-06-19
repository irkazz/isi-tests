import requests
from selenium.webdriver.common.by import By
from .base_page import BasePage


class PayersPage(BasePage):
    PAGE_URL = BasePage.BASE_URL + "accounts"
    ADD_PAYER = (By.CSS_SELECTOR, "div.new-design-plus")
    SEARCH_PAYER_INPUT = (By.CSS_SELECTOR, "input[name='searchAccount']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, login_page):
        # Navigate to a webpage
        login_page.login()
        assert self.wait_for_element_visible((By.CSS_SELECTOR, "img.brand-logo-img"))
        self.driver.get(self.PAGE_URL)
        self.wait_for_element_present(self.ADD_PAYER)

    def click_new_payer(self):
        self.find_element(self.ADD_PAYER).click()

    def get_search_response_for_new_payer(self, id):
        url = f"https://test.isi-technology.com:8000/api/v1/accounts/account/?show_inactive=no&limit=20&offset=0&search={id}"
        headers = {
            "Authorization": "Token 6a2a35d809d5482a556acb870c58a9bac12fd85a",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        return response

