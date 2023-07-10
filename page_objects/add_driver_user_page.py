from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_objects.add_user_page import AddUser


class AddDriverUser(AddUser):
    # driver fields
    # TODO: Extract Driver related locators, constants and methods into separate file, by user type, can be easily updated
    DRIVER_TYPE_SELECT = (By.CSS_SELECTOR, "select[name='driver_type']")
    BIRTHDAY_INPUT = (By.CSS_SELECTOR, "input[placeholder='Birthday, date']")
    LICENSE_EXPIRATION_INPUT = (By.CSS_SELECTOR, "input[name='license_expiration']")
    LICENSE_NUMBER_INPUT = (By.CSS_SELECTOR, "input[name='license']")
    LICENSE_TYPE_SELECT = (By.CSS_SELECTOR, "select[name='license_type']")
    DRIVER_HIRE_DATE_INPUT = (By.CSS_SELECTOR, "input[name='hire']")
    DRIVER_SEE_ORDERS_SELECT = (By.CSS_SELECTOR, "select[name='see_available_orders']")

    # driver constants
    BIRTHDAY = "01/10/1980"
    LICENCE_EXPIRATION_DATE = "01/10/2030"
    LICENSE_NUMBER = "A123BCD"
    LICENCE_TYPE_TEXT = "C"
    DRIVER_HIRE_DATE = "01/10/2020"

    # Common methods
    def __init__(self, driver):
        super().__init__(driver)
        self.DRIVER_USERNAME = "dr" + self.TIMESTAMP

    # driver methods
    def select_driver_type(self, select_text="Employee"):
        select_element = self.find_element(self.DRIVER_TYPE_SELECT)
        select = Select(select_element)
        select.select_by_visible_text(select_text)

    def enter_birthday(self, birthday=BIRTHDAY):
        self.find_element(self.BIRTHDAY_INPUT).send_keys(birthday)

    def enter_license_expiration(self, expiration_date=LICENCE_EXPIRATION_DATE):
        self.find_element(self.LICENSE_EXPIRATION_INPUT).send_keys(expiration_date)

    def enter_license_number(self, license_number=LICENSE_NUMBER):
        self.find_element(self.LICENSE_NUMBER_INPUT).send_keys(license_number)

    def select_license_type(self, select_text=LICENCE_TYPE_TEXT):
        select_element = self.find_element(self.LICENSE_TYPE_SELECT)
        select = Select(select_element)
        select.select_by_visible_text(select_text)

    def enter_driver_hire_date(self, hire_date=DRIVER_HIRE_DATE):
        self.find_element(self.DRIVER_HIRE_DATE_INPUT).send_keys(hire_date)

    def select_see_orders(self, select_text="Default"):
        select_element = self.find_element(self.DRIVER_SEE_ORDERS_SELECT)
        select = Select(select_element)
        select.select_by_visible_text(select_text)

    # TODO: move it to the utils class, refactor to have getResponse call
    def logout_user(self):
        self.user_logout()

    def create_new_driver_user(self):
        self.enter_firstname()
        self.enter_lastname()
        self.select_profile("Driver")
        self.select_driver_type()
        self.enter_address1()
        self.enter_birthday()
        self.enter_phone1()
        self.enter_license_expiration()
        self.enter_license_number()
        self.select_license_type()
        self.enter_driver_hire_date()
        self.select_see_orders()
        self.enter_email()
        self.enter_username(self.DRIVER_USERNAME)
        self.enter_password()
        self.enter_confirm_password()
        self.click_save_user_button()
        return self.DRIVER_USERNAME
