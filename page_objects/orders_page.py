from selenium.webdriver.common.by import By

from config import BASE_PAGE_URL
from .base_page import BasePage


class OrdersPage(BasePage):
    PAGE_URL = BASE_PAGE_URL + "orders"
    ADD_ORDER = (By.CSS_SELECTOR, "div[ng-click='superAddNewOrder();']")
    SEARCH_ORDER_INPUT = (By.CSS_SELECTOR, "input[name='searchOrder']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, login_page):
        # Navigate to a webpage
        login_page.login()
        assert self.wait_for_element_visible((By.CSS_SELECTOR, "img.brand-logo-img"))
        self.driver.get(self.PAGE_URL)
        self.wait_for_element_present(self.ADD_ORDER)

    def click_new_order(self):
        self.wait_for_element_present(self.ADD_ORDER).click()

    # TODO: change end point
    def get_search_response_for_new_order(self, order_id, order_date):
        return self.api_requests.get_search_response(f"https://test.isi-technology.com:8000/api/v1/orders/reservation"
                                                     f"/?limit=20&offset=0&search={order_id}&search_type=account"
                                                     f"&statuses=0,1,2,3,4,5,6,7,8,9,10,&custom_trip_types=1,2,3,4,5,"
                                                     f"6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,"
                                                     f"28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,&attentions=0,"
                                                     f"1,2,3,4,5,6,7,8,fav,9,10,11,12,13,15,16,17,18,19,20,21,22,23,"
                                                     f"24,-1,&start={order_date}&end={order_date}&fast=true")
