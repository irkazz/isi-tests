import pytest
import sys

from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage
from utils.api_requests import API

from utils.webdriver_utils import WebDriverUtils
from tests.fixtures import driver, login_page

sys.path.append("C:/Users/irkaz/ISI_Sample_Tests")


@pytest.mark.login
@pytest.mark.basic
def test_login_success(login_page):
    login_page.login()
    assert login_page.wait_for_element_visible((By.CSS_SELECTOR, "img.brand-logo-img"))

@pytest.mark.basic
def test_api_login_success():
    api_req = API()
    api_req.user_login()
    assert api_req.token is not None


# Teardown - quit the driver if the test module execution is interrupted or encounters an error
def pytest_unconfigure(config):
    driver = config.driver
    if driver is not None:
        driver.quit()
