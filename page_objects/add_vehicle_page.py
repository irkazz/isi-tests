from datetime import datetime, timedelta

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_objects.login_page import LoginPage
from page_objects.vehicles_page import VehiclesPage


class AddVehicle(VehiclesPage):
    VEHICLE_KIND_SELECT = (By.CSS_SELECTOR, "select[name='kind']")
    DATE_ACTIVATED_INPUT = (By.CSS_SELECTOR, "input[name='day_activated']")
    VEHICLE_MODEL_SELECT = (By.CSS_SELECTOR, "select[name='model_type']")

    VEHICLE_ID_INPUT = (By.CSS_SELECTOR, "input[name='vehicle_id']")
    VEHICLE_MAKE_INPUT = (By.CSS_SELECTOR, "input[name='make']")
    VEHICLE_MODEL_INPUT = (By.CSS_SELECTOR, "input[name='model_name']")
    VEHICLE_YEAR_INPUT = (By.CSS_SELECTOR, "input[name='year']")
    VEHICLE_VIN_INPUT = (By.CSS_SELECTOR, "input[name='vin']")  # 17
    VEHICLE_PLATE_INPUT = (By.CSS_SELECTOR, "input[name='plate']")  # 4
    VEHICLE_COLOR_INPUT = (By.CSS_SELECTOR, "input[name='color']")
    VEHICLE_MILEAGE_INPUT = (By.CSS_SELECTOR, "input[name='mileage']")  # limit is too high
    VEHICLE_REGISTRATION_DATE_INPUT = (By.CSS_SELECTOR, "input[name='registration_date']")
    VEHICLE_PURCHASE_DATE_INPUT = (By.CSS_SELECTOR, "input[name='purchase_date']")

    CAPACITY_TAB = (By.CSS_SELECTOR, "li[heading='*Capacity']>a")

    ADD_PLACE_ICON = (By.CSS_SELECTOR, "span[ng-click*='addGroup']")  #have to use xpath to locate the element
    AMBULATORY_CAPACITY = (By.CSS_SELECTOR,"div.form-group")

    SAVE_BUTTON = (By.CSS_SELECTOR, "button[ng-click='saveVehicle()']")

    # common constants
    TIMESTAMP = datetime.now().strftime("%Y%m%d%H%M%S")
    VEHICLE_DATE_ACTIVATED = datetime.now().strftime("%m/%d/%Y")
    VEHICLE_ID = "I" + TIMESTAMP
    VEHICLE_MAKE = "MAKE" + TIMESTAMP
    VEHICLE_MODEL = "MODEL" + TIMESTAMP
    VEHICLE_YEAR = "2020"
    VEHICLE_VIN = "1" * 17  # length = 17
    VEHICLE_PLATE = "1" * 4  # min = 4
    VEHICLE_COLOR = "Red"
    VEHICLE_MILEAGE = "1000"
    VEHICLE_REGISTRATION_DATE = (datetime.now()-timedelta(days=3)).strftime("%m/%d/%Y")
    VEHICLE_PURCHASE_DATE = VEHICLE_REGISTRATION_DATE

    # Common methods
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(driver)

    # TODO: Make util or base class method
    def select_kind(self, select_text="Contractor"):
        select_element = self.find_element(self.VEHICLE_KIND_SELECT)
        select = Select(select_element)
        select.select_by_visible_text(select_text)

    def enter_date_activated(self, date=VEHICLE_DATE_ACTIVATED):
        self.find_element(self.DATE_ACTIVATED_INPUT).send_keys(date)

    def select_model_type(self, select_text="Bus"):
        select_element = self.find_element(self.VEHICLE_MODEL_SELECT)
        select = Select(select_element)
        select.select_by_visible_text(select_text)

    def enter_id(self, vehicle_id=VEHICLE_ID):
        self.find_element(self.VEHICLE_ID_INPUT).send_keys(vehicle_id)

    def enter_make(self, make=VEHICLE_MAKE):
        self.find_element(self.VEHICLE_MAKE_INPUT).send_keys(make)

    def enter_model(self, model=VEHICLE_MODEL):
        self.find_element(self.VEHICLE_MODEL_INPUT).send_keys(model)

    def enter_year(self, year=VEHICLE_YEAR):
        self.find_element(self.VEHICLE_YEAR_INPUT).send_keys(year)

    def enter_vin(self, vin=VEHICLE_VIN):
        self.find_element(self.VEHICLE_VIN_INPUT).send_keys(vin)

    def enter_plate(self, plate=VEHICLE_PLATE):
        self.find_element(self.VEHICLE_PLATE_INPUT).send_keys(plate)

    def enter_color(self, color=VEHICLE_COLOR):
        self.find_element(self.VEHICLE_COLOR_INPUT).send_keys(color)

    def enter_mileage(self, mileage=VEHICLE_MILEAGE):
        self.find_element(self.VEHICLE_MILEAGE_INPUT).send_keys(mileage)

    def enter_registration_date(self, registration_date=VEHICLE_REGISTRATION_DATE):
        self.find_element(self.VEHICLE_REGISTRATION_DATE_INPUT).send_keys(registration_date)

    def enter_purchase_date(self, purchase_date=VEHICLE_PURCHASE_DATE):
        self.find_element(self.VEHICLE_PURCHASE_DATE_INPUT).send_keys(purchase_date)

    def switch_to_capacity_tab(self):
        tab = self.find_element(self.CAPACITY_TAB)
        self.driver.execute_script("arguments[0].click();", tab)
        self.wait_for_element_present(self.ADD_PLACE_ICON)

    def add_capacity(self):
        add_cap = self.find_element(self.ADD_PLACE_ICON)
        self.driver.execute_script("arguments[0].click();", add_cap)
        self.wait_for_element_present(self.AMBULATORY_CAPACITY)

    def click_save_vehicle_button(self):
        self.find_element(self.SAVE_BUTTON).click()
        self.wait_for_element_invisible(self.VEHICLE_KIND_SELECT)
        self.wait_for_element_visible(self.SEARCH_VEHICLE_INPUT)

    def open_add_new_vehicle_form(self):
        self.open_page(self.login_page)
        self.wait_for_element_present(self.VEHICLE_KIND_SELECT)
        self.click_new_vehicle()

    def create_new_vehicle(self):
        self.select_kind()
        self.enter_date_activated()
        self.select_model_type()
        self.enter_id()
        self.enter_make()
        self.enter_model()
        self.enter_year()
        self.enter_vin()
        self.enter_plate()
        self.enter_color()
        self.enter_mileage()
        self.enter_registration_date()
        self.enter_purchase_date()
        self.switch_to_capacity_tab()
        self.add_capacity()
        self.click_save_vehicle_button()
        return self.VEHICLE_ID
