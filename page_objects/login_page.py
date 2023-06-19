from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    PAGE_URL = BasePage.BASE_URL + "login"
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.login-button")
    USERNAME = 'Irina_test'
    PASSWORD = '000000'

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        # Navigate to a webpage
        self.driver.get(self.PAGE_URL)
        self.wait_for_element_present(self.USERNAME_INPUT)

    def enter_username(self, username=USERNAME):
        self.find_element(self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password=PASSWORD):
        self.find_element(self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.find_element(self.LOGIN_BUTTON).click()

    def login(self):
        self.open_page()
        self.enter_username()
        self.enter_password()
        self.click_login()
