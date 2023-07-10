from typing import List

from selenium.webdriver.common.by import By

from config import BASE_URL
from page_objects.base_page import BasePage


# Class NavItem represents navigation item with subitems (if any), URL it references and page title when selected
class NavItem():
    def __init__(self, locator: str, title: str, url: object, sub_items: [] = None):
        self.locator = locator
        self.title = '' if title is None else title
        self.url = '' if url is None else url
        self.sub_items = [] if sub_items is None else sub_items

    # Returns true if it's a top navigation item with sub items
    def is_top_item_with_sub_items(self):
        return len(self.sub_items) > 0

    def get_title(self):
        return self.title

    def get_url(self):
        return self.url

    def get_sub_items(self):
        return self.sub_items


def get_top_item_locator(text):
    # return 'ul.nav > li > a > span:contains("' + text + '")'  # TODO: have one function with class param
    return '//ul[contains(@class, "nav")]/li/a/span[contains(text(), "' + text + '")]'


def get_sub_item_locator(ui_sref):
    locator_details = ui_sref
    return 'ul.sub-menu > li > a[ui-sref= "app.' + ui_sref + '"] > span'


def create_top_item(text: str, title: str = None, url: str = None) -> NavItem:
    if url is not None and title is None:
        title = text.upper()
    return NavItem(get_top_item_locator(text), title, url)


def add_sub_items(sub_item_details) -> List[NavItem]:
    sub_items = []
    for details in sub_item_details:
        # TODO: assuming tuple has 3 items
        locator_text, title, url = details
        sub_item = NavItem(get_sub_item_locator(locator_text), title, url)
        sub_items.append(sub_item)
    return sub_items


class NavPage(BasePage):
    NAV_BAR_TITLE = (By.CSS_SELECTOR, 'p.navbar-text.ng-binding')

    def __init__(self, driver):
        super().__init__(driver)
        self.nav_items = []

    def init_page(self):
        # Create NavItems
        nav_item1 = create_top_item('Dashboard')
        nav_item1.sub_items = add_sub_items([
            ("home", "Dashboard".upper(), BASE_URL)
        ])
        nav_item2 = create_top_item('Dispatching', url=BASE_URL + 'main')
        nav_item3 = create_top_item('Orders')
        nav_item3.sub_items = add_sub_items([
            ("order", "Today's Orders".upper(), BASE_URL + "orders"),
            ("reservation", "Reservations".upper(), BASE_URL + "reservation"),
            ("uploads", "Trip Import".upper(), BASE_URL + "uploads"),
            ("facility", "Facilities", BASE_URL + "facility"),
        ])  # TODO: "Fsilities" title is inconsistent with others, not all upper case

        nav_item4 = create_top_item('Visits', url=BASE_URL + 'visits')
        nav_item5 = create_top_item('Scheduling')
        nav_item5.sub_items = add_sub_items([
            ("preassign-modes", "Pre-Assign Modes".upper(), BASE_URL + "preassign-modes"),
            ("route", "Driver Shifts".upper(), BASE_URL + "shifts"),
            ("route-import", "Shift import".upper(), BASE_URL + "shift-import"),
            ("run", "Routes".upper(), BASE_URL + "runs"),
        ])

        nav_item6 = create_top_item('Vehicles')
        nav_item6.sub_items = add_sub_items([
            ("vehicle", "Vehicles".upper(), BASE_URL + "vehicles"),
            ("maintenance", "VEHICLE MAINTENANCE", BASE_URL + "maintenance"),
            ("depot", "Base Locations".upper(), BASE_URL + "depots")
        ])

        nav_item7 = create_top_item('Users')
        nav_item7.sub_items = add_sub_items([
            ("user", "Users".upper(), BASE_URL + "users"),
            ("hrtab", "Payroll".upper(), BASE_URL + "hrtab"),
            ("group", "Driver Groups".upper(), BASE_URL + "groups")
        ])

        nav_item8 = create_top_item('Passengers')
        nav_item8.sub_items = add_sub_items([
            ("client", "Passengers".upper(), BASE_URL + "clients"),
            ("concern", "Concern", BASE_URL + "concern"),
            # TODO: inconsistent, not self-exploratory title, usability
            ("eligibility", "Eligibility Import".upper(), BASE_URL + "eligibility")
        ])

        nav_item9 = create_top_item('Payers')
        nav_item9.sub_items = add_sub_items([
            ("account", "Payers".upper(), BASE_URL + "accounts"),
            ("invoice", "Billing".upper(), BASE_URL + "invoices"),
            ("item", "Invoice Items".upper(), BASE_URL + "items")
        ])

        nav_item10 = create_top_item('Reports', url=BASE_URL + 'reports')

        nav_item11 = create_top_item('Settings')
        nav_item11.sub_items = add_sub_items([
            ("setting", "SETTINGS",BASE_URL + "settings"),
            ("providers_settings", "Brokers settings".upper(), BASE_URL + "brokers_settings")
        ])

        nav_item12 = create_top_item('Transit')
        nav_item12.sub_items = add_sub_items([
            ("transit_dispatch", "TRANSIT / DISPATCHING", BASE_URL + "transit_dispatch"),
            ("transit_scheduling", "TRANSIT / SCHEDULING", BASE_URL + "transit_scheduling"),
            ("transit_route", "TRANSIT / ROUTES",  BASE_URL + "transit_route"),
            ("transit_stop", "TRANSIT / STOPS",  BASE_URL + "transit_stop"),
            ("transit_pass", "TRANSIT / PASS", BASE_URL + "transit_pass")
        ])

        nav_item13 = create_top_item('Payments', url=BASE_URL + 'payments')

        # Add NavItems to NavPage
        self.nav_items.append(nav_item1)
        self.nav_items.append(nav_item2)
        self.nav_items.append(nav_item3)
        self.nav_items.append(nav_item4)
        self.nav_items.append(nav_item5)
        self.nav_items.append(nav_item6)
        self.nav_items.append(nav_item7)
        self.nav_items.append(nav_item8)
        self.nav_items.append(nav_item9)
        self.nav_items.append(nav_item10)
        self.nav_items.append(nav_item11)
        self.nav_items.append(nav_item12)
        self.nav_items.append(nav_item13)

    def get_items(self) -> List[NavItem]:
        return self.nav_items

    def nav_item_click(self, item: NavItem):
        span = self.wait_for_element_present((By.XPATH, item.locator))
        self.driver.execute_script("arguments[0].click();", span)

    def nav_sub_item_click(self, item: NavItem):
        span = self.wait_for_element_present((By.CSS_SELECTOR, item.locator))
        self.driver.execute_script("arguments[0].click();", span)

    def is_title_text_changed(self, expected_text):
        title = self.wait_for_element_present(self.NAV_BAR_TITLE)
        initial_text = title.text
        if initial_text != expected_text:
            self.wait.until(lambda driver: title.text == expected_text)
        return title.text == expected_text
