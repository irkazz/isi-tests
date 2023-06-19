import requests
from selenium.webdriver.common.by import By
from .base_page import BasePage


class PassengersPage(BasePage):
    PAGE_URL = BasePage.BASE_URL + "clients"
    ADD_PASSENGER = (By.CSS_SELECTOR, "div.new-design-plus")
    SEARCH_PASSENGER_INPUT = (By.CSS_SELECTOR, "input[name='searchClient']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, login_page):
        # Navigate to a webpage
        login_page.login()
        assert self.wait_for_element_visible((By.CSS_SELECTOR, "img.brand-logo-img"))
        self.driver.get(self.PAGE_URL)
        self.wait_for_element_present(self.ADD_PASSENGER)

    def click_new_passenger(self):
        self.find_element(self.ADD_PASSENGER).click()

    def get_search_response_for_new_passenger(self, last_name):
        url = f"https://test.isi-technology.com:8000/api/v1/accounts/client/?limit=20&offset=0&search={last_name}&search_type=client"
        headers = {
            "Authorization": "Token 6a2a35d809d5482a556acb870c58a9bac12fd85a",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        return response

