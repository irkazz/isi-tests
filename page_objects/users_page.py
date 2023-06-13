from selenium.webdriver.common.by import By
from base_page import BasePage
from login_page import LoginPage
from page_objects import add_user_page
from page_objects.add_user_page import AddUser


class UsersPage(BasePage):
    PAGE_URL = BasePage.BASE_URL + "users"
    ADD_USER = (By.CSS_SELECTOR, "div.new-design-plus")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, login_page):
        # Navigate to a webpage
        login_page.login()
        assert self.wait_for_element_visible((By.CSS_SELECTOR, "img.brand-logo-img"))
        self.driver.get(self.PAGE_URL)
        self.wait_for_element_present(self.ADD_USER)

    def click_new_user(self):
        self.find_element(self.ADD_USER).click()
        self.wait_for_element_present(AddUser.AVATAR_IMG)
