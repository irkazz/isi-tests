from datetime import datetime

from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage
from page_objects.payers_page import PayersPage


class AddPayer(PayersPage):
    # common fields
    PAYER_ID_INPUT = (By.CSS_SELECTOR, "input[placeholder='Payer ID']")
    PAYER_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Payer Name']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[ng-click='saveAccount()']")

    # common constants
    TIMESTAMP = datetime.now().strftime("%Y%m%d%H%M%S")
    ID = "ID" + TIMESTAMP
    NAME = "John L" + TIMESTAMP

    # Common methods
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(driver)

    def enter_payer_id(self, id=ID):
        self.find_element(self.PAYER_ID_INPUT).send_keys(id)

    def enter_payer_name(self, name=NAME):
        self.find_element(self.PAYER_NAME_INPUT).send_keys(name)

    def click_save_payer_button(self):
        save = self.find_element(self.SAVE_BUTTON)
        self.driver.execute_script("arguments[0].click();", save)
        self.wait_for_element_invisible(self.PAYER_ID_INPUT)
        self.wait_for_element_visible(self.SEARCH_PAYER_INPUT)

    def open_add_new_payer_form(self):
        self.open_page(self.login_page)
        self.wait_for_element_present(self.SEARCH_PAYER_INPUT)
        self.click_new_payer()
        self.wait_for_element_present(self.PAYER_ID_INPUT)

    def create_new_payer(self):
        self.enter_payer_id()
        self.enter_payer_name()
        self.click_save_payer_button()
        return self.ID
