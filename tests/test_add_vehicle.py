import pytest

from page_objects.add_passenger_page import AddPassenger
from page_objects.add_vehicle_page import AddVehicle

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
def add_vehicle_page(driver):
    # Setup - instantiate the page_objects class
    page = AddVehicle(driver)
    yield page


@pytest.mark.vehicles
def test_add_vehicle(add_vehicle_page):
    add_vehicle_page.open_add_new_vehicle_form()
    vehicle_id = add_vehicle_page.create_new_vehicle()
    response = add_vehicle_page.get_search_response_for_new_vehicle(vehicle_id)

    if response.status_code == 200:
        data = response.json()
        assert len(data["results"]) == 1
    else:
        print(f"Error: {response.status_code} - {response.text}")


