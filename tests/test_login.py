import pytest
import sys

from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage


from utils.webdriver_utils import WebDriverUtils

sys.path.append("C:/Users/irkaz/ISI_Sample_Tests")


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


@pytest.mark.login
def test_login_success(login_page):
    login_page.login()
    assert login_page.wait_for_element_visible((By.CSS_SELECTOR, "img.brand-logo-img"))


# Teardown - quit the driver if the test module execution is interrupted or encounters an error
def pytest_unconfigure(config):
    driver = config.driver
    if driver is not None:
        driver.quit()
