from datetime import datetime

from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage
from page_objects.passengers_page import PassengersPage


class AddPassenger(PassengersPage):
    # common fields
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='First Name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    DATE_OF_BIRTH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Date']")
    ADDRESS1_INPUT = (By.CSS_SELECTOR, "input[name='address_1']")
    PHONE1_INPUT = (By.CSS_SELECTOR, "input[name='phone_1']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[ng-click='saveClient()']")

    # common constants
    TIMESTAMP = datetime.now().strftime("%Y%m%d%H%M%S")
    FIRST_NAME = "Fname" + TIMESTAMP
    LAST_NAME = "Lname" + TIMESTAMP
    ADDRESS1 = "123 Princeton Ct, Buffalo, NY 14225, USA"
    ADDRESS_SELECT = (By.CSS_SELECTOR, "a[title='" + ADDRESS1 + "']")
    PHONE1 = "1234567890"
    DATE_OF_BIRTH = "11/12/1990"

    # Common methods
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(driver)
        self.passengers_page = PassengersPage(driver)

    def enter_firstname(self, first_name=FIRST_NAME):
        self.find_element(self.FIRST_NAME_INPUT).send_keys(first_name)

    def enter_lastname(self, last_name=LAST_NAME):
        self.find_element(self.LAST_NAME_INPUT).send_keys(last_name)

    def enter_date_of_birth(self, date=DATE_OF_BIRTH):
        self.find_element(self.DATE_OF_BIRTH_INPUT).send_keys(date)

    def enter_address1(self, address1=ADDRESS1):
        self.find_element(self.ADDRESS1_INPUT).send_keys(address1)
        select = self.wait_for_element_present(self.ADDRESS_SELECT)
        select.click()

    def enter_phone1(self, phone1=PHONE1):
        self.find_element(self.PHONE1_INPUT).send_keys(phone1)

    def click_save_passenger_button(self):
        self.find_element(self.SAVE_BUTTON).click()
        self.wait_for_element_invisible(self.FIRST_NAME_INPUT)
        self.wait_for_element_visible(self.passengers_page.SEARCH_PASSENGER_INPUT)

    def open_add_new_passenger_form(self):
        self.passengers_page.open_page(self.login_page)
        self.wait_for_element_visible(self.SEARCH_PASSENGER_INPUT)
        self.passengers_page.click_new_passenger()

    def create_new_passenger(self):
        self.enter_firstname()
        self.enter_lastname()
        self.enter_date_of_birth()
        self.enter_address1()
        self.enter_phone1()
        self.click_save_passenger_button()
        return self.LAST_NAME
