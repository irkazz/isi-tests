import pytest

from page_objects.add_driver_user_page import AddDriverUser
from page_objects.add_user_page import AddUser

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
def add_user_page(driver):
    # Setup - instantiate the page_objects class
    page = AddUser(driver)
    yield page

@pytest.fixture
def add_driver_user_page(driver):
    # Setup - instantiate the page_objects class
    page = AddDriverUser(driver)
    yield page

@pytest.mark.users
def test_add_admin_user(add_user_page):
    add_user_page.open_add_new_user_form()
    username = add_user_page.create_new_admin_user()
    response = add_user_page.get_search_response_for_new_user(username)

    if response.status_code == 200:
        data = response.json()
        assert len(data["results"]) == 1
    else:
        print(f"Error: {response.status_code} - {response.text}")
    # add_user_page.logout_user()

@pytest.mark.users
def test_add_driver_user(add_user_page, add_driver_user_page):
    add_user_page.open_add_new_user_form()
    username = add_driver_user_page.create_new_driver_user()
    response = add_user_page.get_search_response_for_new_user(username)

    if response.status_code == 200:
        data = response.json()
        assert len(data["results"]) == 1
    else:
        print(f"Error: {response.status_code} - {response.text}")
    #add_user_page.logout_user()
