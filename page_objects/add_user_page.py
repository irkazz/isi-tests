from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page import BasePage


class AddUser(BasePage):
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='First Name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    PROFILE_TYPE_SELECT = (By.CSS_SELECTOR, "select[name='profile_type']")
    ADDRESS1_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address #1']")
    PHONE1_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone #1']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='Email']")
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Password']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Confirm Password']")

    TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    FIRST_NAME = "Fname" + TIMESTAMP
    LAST_NAME = "Lname" + TIMESTAMP
    SELECT_VALUE = "number:0"
    AVATAR_IMG = (By.CSS_SELECTOR, "img#avatar")
    ADDRESS1 = "1, Main st."
    PHONE1 = "1234567890"
    EMAIL = "testuser@gmail.com"
    USERNAME = "testuser" + TIMESTAMP
    PASSWORD = "123456"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_firstname(self, first_name=FIRST_NAME):
        self.find_element(self.FIRST_NAME_INPUT).send_keys(first_name)

    def enter_lastname(self, last_name=LAST_NAME):
        self.find_element(self.LAST_NAME_INPUT).send_keys(last_name)

    def select_profile(self, select_value=SELECT_VALUE):
        select_element = self.find_element(self.PROFILE_TYPE_SELECT)
        select = Select(select_element)
        select.select_by_value(select_value)

    def enter_address1(self, address1=ADDRESS1):
        self.find_element(self.ADDRESS1_INPUT).send_keys(address1)

    def enter_phone1(self, phone1=PHONE1):
        self.find_element(self.PHONE1_INPUT).send_keys(phone1)

    def enter_email(self, email=EMAIL):
        self.find_element(self.EMAIL_INPUT).send_keys(email)

    def enter_username(self, username=USERNAME):
        self.find_element(self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password=PASSWORD):
        password_element = self.find_element(self.PASSWORD_INPUT)
        # self.driver.execute_script("arguments[0].setAttribute('type', 'text');", password_element)
        # self.driver.execute_script("arguments[0].value = '" + password + "';", password_element)
        action = ActionChains(self.driver)
        action.send_keys_to_element(password_element, password).perform()
        # self.driver.execute_script("arguments[0].setAttribute('type', 'password');", password_element)

    def enter_confirm_password(self, password=PASSWORD):
        password_element = self.find_element(self.CONFIRM_PASSWORD_INPUT)
        # self.driver.execute_script("arguments[0].setAttribute('type', 'text');", password_element)
        # self.driver.execute_script("arguments[0].value = '" + password + "';", password_element)
        # self.driver.execute_script("arguments[0].setAttribute('type', 'password');", password_element)
        action = ActionChains(self.driver)
        action.send_keys_to_element(password_element, password).perform()