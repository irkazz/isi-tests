import pytest

from page_objects.add_user_page import AddUser
from page_objects.login_page import LoginPage
from page_objects.users_page import UsersPage

from utils.webdriver_utils import WebDriverUtils


@pytest.fixture(scope="module")
def driver():
    utils = WebDriverUtils()
    utils.create_driver()
    driver = utils.driver

    yield driver
    # Teardown - quit the driver after all tests in the module have finished
    utils.quit_driver()

@pytest.fixture
def login_page(driver):
    # Setup - instantiate the page_objects class
    page = LoginPage(driver)
    yield page

@pytest.fixture
def users_page(driver):
    # Setup - instantiate the page_objects class
    page = UsersPage(driver)
    yield page

@pytest.fixture
def add_user_page(driver):
    # Setup - instantiate the page_objects class
    page = AddUser(driver)
    yield page

@pytest.mark.users
def test_add_user(add_user_page, users_page, login_page):
    users_page.open_page(login_page)
    users_page.click_new_user()
    add_user_page.enter_firstname()
    add_user_page.enter_lastname()
    add_user_page.select_profile()
    add_user_page.enter_address1()
    add_user_page.enter_phone1()
    add_user_page.enter_email()
    add_user_page.enter_username()
    add_user_page.enter_password()
    add_user_page.enter_confirm_password()
    print('blah')
