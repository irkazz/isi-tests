import pytest

from page_objects.add_payer_page import AddPayer

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
def add_payer_page(driver):
    # Setup - instantiate the page_objects class
    page = AddPayer(driver)
    yield page


@pytest.mark.passengers
def test_add_payer(add_payer_page):
    add_payer_page.open_add_new_payer_form()
    payer_id = add_payer_page.create_new_payer()
    response = add_payer_page.get_search_response_for_new_payer(payer_id)

    if response.status_code == 200:
        data = response.json()
        assert len(data["results"]) == 1
    else:
        print(f"Error: {response.status_code} - {response.text}")


