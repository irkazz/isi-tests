import pytest

from page_objects.add_passenger_page import AddPassenger

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
def add_passenger_page(driver):
    # Setup - instantiate the page_objects class
    page = AddPassenger(driver)
    yield page


@pytest.mark.passengers
def test_add_passenger(add_passenger_page):
    add_passenger_page.open_add_new_passenger_form()
    last_name = add_passenger_page.create_new_passenger()
    response = add_passenger_page.get_search_response_for_new_passenger(last_name)

    if response.status_code == 200:
        data = response.json()
        assert len(data["results"]) == 1
    else:
        print(f"Error: {response.status_code} - {response.text}")
    # add_user_page.logout_user()


