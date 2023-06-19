import requests
from selenium.webdriver.common.by import By
from .base_page import BasePage


class UsersPage(BasePage):
    PAGE_URL = BasePage.BASE_URL + "users"
    ADD_USER = (By.CSS_SELECTOR, "div.new-design-plus")
    SEARCH_USER_INPUT = (By.CSS_SELECTOR, "input[name='searchUser']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, login_page):
        # Navigate to a webpage
        login_page.login()
        assert self.wait_for_element_visible((By.CSS_SELECTOR, "img.brand-logo-img"))
        self.driver.get(self.PAGE_URL)
        self.wait_for_element_present(self.ADD_USER)

    def click_new_user(self):
        self.find_element(self.ADD_USER).click()

    def get_search_response_for_new_user(self, username):
        url = f"https://test.isi-technology.com:8000/api/v1/accounts/profile_table/?limit=20&offset=0&search={username}&search_type=user"
        headers = {
            "Authorization": "Token 6a2a35d809d5482a556acb870c58a9bac12fd85a",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        return response

    def user_logout(self):
        url = "https://test.isi-technology.com:8000/api/v1/account/staff_logout/"
        headers = {
            "Authorization": "Token 6a2a35d809d5482a556acb870c58a9bac12fd85a",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers)
        assert response.status_code == 200
