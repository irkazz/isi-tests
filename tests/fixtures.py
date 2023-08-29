import unittest

import pytest

from page_objects.add_driver_user_page import AddDriverUser
from page_objects.add_order_page import AddOrder
from page_objects.add_passenger_page import AddPassenger
from page_objects.add_payer_page import AddPayer
from page_objects.add_user_page import AddUser
from page_objects.add_vehicle_page import AddVehicle
from page_objects.login_page import LoginPage
from page_objects.navigation_page import NavPage
from utils.api_requests import API
from utils.webdriver_utils import WebDriverUtils
from utils.validators import Validator


@pytest.fixture(scope="module")
def driver():
    utils = WebDriverUtils()
    utils.create_driver()
    driver = utils.driver

    yield driver

@pytest.fixture
def login_page(driver):
    # Setup - instantiate the page_objects class
    page = LoginPage(driver)
    yield page

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


@pytest.fixture
def api_validator():
    # Setup - instantiate the validator class
    api_validator = Validator()
    yield api_validator


@pytest.fixture
def add_payer_page(driver):
    # Setup - instantiate the page_objects class
    page = AddPayer(driver)
    yield page


@pytest.fixture
def add_vehicle_page(driver):
    # Setup - instantiate the page_objects class
    page = AddVehicle(driver)
    yield page


@pytest.fixture
def add_passenger_page(driver):
    # Setup - instantiate the page_objects class
    page = AddPassenger(driver)
    yield page


@pytest.fixture
def login_page(driver):
    # Setup - instantiate the page_objects class
    page = LoginPage(driver)
    yield page


@pytest.fixture
def navigation_page(driver):
    # Setup - instantiate the page_objects class
    page = NavPage(driver)
    yield page

@pytest.fixture
def api_request():
    api_request = API()
    yield api_request