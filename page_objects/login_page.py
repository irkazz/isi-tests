from selenium.webdriver.common.by import By

from config import BASE_PAGE_URL, DEFAULT_PASSWORD, DEFAULT_USERNAME
from .base_page import BasePage


class LoginPage(BasePage):
    PAGE_URL = BASE_PAGE_URL + "login"
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        # Navigate to a webpage
        self.driver.get(self.PAGE_URL)
        self.wait_for_element_present(self.USERNAME_INPUT)

    def enter_username(self, username=DEFAULT_USERNAME):
        self.find_element(self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password=DEFAULT_PASSWORD):
        self.find_element(self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.find_element(self.LOGIN_BUTTON).click()

    def login(self):
        self.open_page()
        self.enter_username()
        self.enter_password()
        self.click_login()
