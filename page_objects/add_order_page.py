from datetime import datetime, timedelta

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_objects.login_page import LoginPage
from page_objects.orders_page import OrdersPage


class AddOrder(OrdersPage):
    SEARCH_DROPDOWN = (By.CSS_SELECTOR, "ul.dropdown-menu.ng-isolate-scope")
    PAYER_ID_INPUT = (By.CSS_SELECTOR, "input[name='account'][autocomplete='off']")
    PASSENGER_LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    PU_ADDRESS_INPUT = (By.CSS_SELECTOR, "input[name='pick_up_address'][autocomplete='off']")
    DO_ADDRESS_INPUT = (By.CSS_SELECTOR, "input[name='drop_off_address'][autocomplete='off']")
    PICKUP_DATE_INPUT = (By.CSS_SELECTOR, "input[name='mainOrder_initial_time']")
    PICKUP_TYPE_INPUT_HOURS = (By.CSS_SELECTOR, "table[name='mainOrder_initial_hours'] input[placeholder='HH']")
    APP_TYPE_INPUT_HOURS = (By.CSS_SELECTOR, "table[name='mainOrder_appointment_hours'] input[placeholder='HH']")
    PAYMENT_TYPE_SELECT = (By.CSS_SELECTOR, "select[name='payment_method']")

    # TODO: Might be unstable due to spaces, need to figure out how to fix
    PU_ADDRESS = "1001 Main St, Buffalo, NY 14203 , USA"
    DO_ADDRESS = "100 Main St, Buffalo, NY 14202, USA"
    PICKUP_DATE = datetime.now().strftime("%m/%d/%Y")
    PICKUP_TIME = "11"
    APP_TIME = "12"
    PAYMENT_TYPE = "Voucher"

    SAVE_BUTTON = (By.CSS_SELECTOR, " button[title='Save']")

    def __init__(self, driver, payer_data, passenger_data):
        super().__init__(driver)
        self.login_page = LoginPage(driver)
        self.payer_data = payer_data
        self.passenger_data = passenger_data

    def open_select_dropdown(self, element_locator, text):
        element = self.wait_for_element_present(element_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        element.send_keys(text)
        self.wait_for_element_present(self.SEARCH_DROPDOWN)

    def open_select_payer_dropdown(self):
        self.open_select_dropdown(self.PAYER_ID_INPUT, self.payer_data['account_id'])

    def get_payer_search_link(self):
        payer_value = self.payer_data['account_id']
        return By.CSS_SELECTOR, f"a[title='{payer_value}']"

    def open_select_passenger_dropdown(self):
        self.open_select_dropdown(self.PASSENGER_LAST_NAME_INPUT, self.passenger_data['last_name'])

    def get_passenger_search_link(self):
        passenger_value = self.passenger_data['last_name']
        return By.CSS_SELECTOR, f"a[title*='{passenger_value}']"

    def select_payer(self):
        self.wait_for_element_present(self.get_payer_search_link()).click()
        self.wait_for_element_present(self.PASSENGER_LAST_NAME_INPUT)

    def select_passenger(self):
        self.wait_for_element_present(self.get_passenger_search_link()).click()
        self.wait_for_element_present(self.PU_ADDRESS_INPUT)

    def open_select_pu_address_dropdown(self):
        self.open_select_dropdown(self.PU_ADDRESS_INPUT, self.PU_ADDRESS)

    def get_pu_address_search_link(self):
        pu_address_value = self.PU_ADDRESS
        return By.CSS_SELECTOR, f"a[title='{pu_address_value}']"

    def select_pu_address(self):
        self.wait_for_element_present(self.get_pu_address_search_link()).click()
        self.wait_for_text_in_element_present(self.PU_ADDRESS_INPUT, self.PU_ADDRESS)

    def open_select_do_address_dropdown(self):
        self.open_select_dropdown(self.DO_ADDRESS_INPUT, self.DO_ADDRESS)

    def get_do_address_search_link(self):
        do_address_value = self.DO_ADDRESS
        return By.CSS_SELECTOR, f"a[title='{do_address_value}']"

    def select_do_address(self):
        self.wait_for_element_present(self.get_do_address_search_link()).click()
        self.wait_for_text_in_element_present(self.DO_ADDRESS_INPUT, self.DO_ADDRESS)

    def enter_pickup_date(self):
        self.find_element(self.PICKUP_DATE_INPUT).send_keys(self.PICKUP_DATE)

    def enter_pickup_hours(self):
        self.find_element(self.PICKUP_TYPE_INPUT_HOURS).send_keys(self.PICKUP_TIME)

    def enter_app_hours(self):
        self.find_element(self.APP_TYPE_INPUT_HOURS).send_keys(self.APP_TIME)

    def select_payment_type(self):
        select_element = self.find_element(self.PAYMENT_TYPE_SELECT)
        select = Select(select_element)
        select.select_by_visible_text(self.PAYMENT_TYPE)

    def click_save_button(self):
        self.find_element(self.SAVE_BUTTON).click()
        # we need to wait for page refresh, waiting for user search element should be ok
        self.wait_for_element_invisible(self.SAVE_BUTTON)
        self.wait_for_element_visible(self.SEARCH_ORDER_INPUT)

    def open_add_new_order_form(self):
        self.open_page(self.login_page)
        self.wait_for_element_present(self.SEARCH_ORDER_INPUT)
        self.click_new_order()

    # need the date to check that order was created
    def get_pickup_date(self):
        return self.PICKUP_DATE

    def create_new_order(self):
        self.open_select_payer_dropdown()
        self.select_payer()
        self.open_select_passenger_dropdown()
        self.select_passenger()
        self.open_select_pu_address_dropdown()
        self.select_pu_address()
        self.open_select_do_address_dropdown()
        self.select_do_address()
        self.enter_pickup_date()
        self.enter_pickup_hours()
        self.enter_app_hours()
        self.select_payment_type()
        self.click_save_button()
        print("x")
        # return self.VEHICLE_ID
