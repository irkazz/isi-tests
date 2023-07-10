from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_objects.login_page import LoginPage
from page_objects.users_page import UsersPage


class AddUser(UsersPage):
    # common fields
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='First Name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    PROFILE_TYPE_SELECT = (By.CSS_SELECTOR, "select[name='profile_type']")
    ADDRESS1_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address #1']")
    PHONE1_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone #1']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='Email']")
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Password']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Confirm Password']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[ng-click='saveUser()']")

    # common constants
    TIMESTAMP = datetime.now().strftime("%Y%m%d%H%M%S")
    FIRST_NAME = "Fname" + TIMESTAMP
    LAST_NAME = "Lname" + TIMESTAMP
    AVATAR_IMG = (By.CSS_SELECTOR, "img#avatar")
    ADDRESS1 = "1001 Main St, Buffalo, NY 14203, USA"
    ADDRESS_SELECT = (By.CSS_SELECTOR, "a[title='" + ADDRESS1 + "']")
    PHONE1 = "1234567890"
    EMAIL = "testuser@gmail.com"
    ADMIN_USERNAME = "ad" + TIMESTAMP
    PASSWORD = "123456"

    # Common methods
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(driver)

    def enter_firstname(self, first_name=FIRST_NAME):
        self.find_element(self.FIRST_NAME_INPUT).send_keys(first_name)

    def enter_lastname(self, last_name=LAST_NAME):
        self.find_element(self.LAST_NAME_INPUT).send_keys(last_name)

    def select_profile(self, select_text="Administrator"):
        select_element = self.find_element(self.PROFILE_TYPE_SELECT)
        select = Select(select_element)
        select.select_by_visible_text(select_text)

    def enter_address1(self, address1=ADDRESS1):
        self.find_element(self.ADDRESS1_INPUT).send_keys(address1)
        select = self.wait_for_element_present(self.ADDRESS_SELECT)
        select.click()
        # self.wait.until(lambda driver: self.find_element(self.ADDRESS1_INPUT).text == address1)
        # TODO: might want to add wait or check, this check does not work

    def enter_phone1(self, phone1=PHONE1):
        self.find_element(self.PHONE1_INPUT).send_keys(phone1)

    def enter_email(self, email=EMAIL):
        self.find_element(self.EMAIL_INPUT).send_keys(email)

    def enter_username(self, username):
        self.find_element(self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password=PASSWORD):
        password_element = self.find_element(self.PASSWORD_INPUT)
        action = ActionChains(self.driver)
        action.send_keys_to_element(password_element, password).perform()

    def enter_confirm_password(self, password=PASSWORD):
        password_element = self.find_element(self.CONFIRM_PASSWORD_INPUT)
        action = ActionChains(self.driver)
        action.send_keys_to_element(password_element, password).perform()

    def click_save_user_button(self):
        self.find_element(self.SAVE_BUTTON).click()
        # we need to wait for page refresh, waiting for user search element should be ok
        self.wait_for_element_invisible(self.AVATAR_IMG)
        self.wait_for_element_visible(self.SEARCH_USER_INPUT)

    def open_add_new_user_form(self):
        self.open_page(self.login_page)
        self.wait_for_element_present(self.AVATAR_IMG)
        self.click_new_user()

    # TODO: refactor and have admin user creation in separate class,
    # also see what to extract into separate method and reuse for all user types
    def create_new_admin_user(self):
        self.enter_firstname()
        self.enter_lastname()
        self.select_profile()
        self.enter_address1()
        self.enter_phone1()
        self.enter_email()
        self.enter_username(self.ADMIN_USERNAME)
        self.enter_password()
        self.enter_confirm_password()
        self.click_save_user_button()
        return self.ADMIN_USERNAME
