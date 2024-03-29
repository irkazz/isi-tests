from selenium.webdriver.common.by import By

from config import BASE_PAGE_URL
from .base_page import BasePage


class VehiclesPage(BasePage):
    PAGE_URL = BASE_PAGE_URL + "vehicles"
    ADD_VEHICLE = (By.CSS_SELECTOR, "div.new-design-plus.wrapper-add_vehicle")
    SEARCH_VEHICLE_INPUT = (By.CSS_SELECTOR, "input[name='filter_search']")

    def __init__(self, driver):
        super().__init__(driver)

    #TODO: Move to base page
    def open_page(self, login_page):
        # Navigate to a webpage
        login_page.login()
        assert self.wait_for_element_visible((By.CSS_SELECTOR, "img.brand-logo-img"))
        self.driver.get(self.PAGE_URL)
        self.wait_for_element_present(self.ADD_VEHICLE)

    def click_new_vehicle(self):
        self.find_element(self.ADD_VEHICLE).click()

    def get_search_response_for_new_vehicle(self, vehicle_id):
        return self.api_requests.get_search_response(f"https://test.isi-technology.com:8000/api/v1/vehicles/vehicle"
                                                     f"/?show_archived=no&search={vehicle_id}&search_type=vehicle_id&limit=20&offset=0")
