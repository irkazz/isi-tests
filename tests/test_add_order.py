import time
import pytest

from page_objects.add_order_page import AddOrder
from tests.fixtures import driver, api_request, api_validator


def add_passenger_api(api_request, api_validator):
    # Generate timestamp
    timestamp = str(int(time.time()))
    response = api_request.create_passenger_api(timestamp)
    return api_validator.validate_client_created(response, timestamp)


def add_payer_api(api_request, api_validator):
    # Generate timestamp
    timestamp = str(int(time.time()))
    response = api_request.create_payer_api(timestamp)
    return api_validator.validate_acc_created(response, timestamp)


def deactivate_payer_api(api_request, api_validator, payer_id):
    response = api_request.deactivate_payer_api(payer_id)
    api_validator.validate_object_deactivated(response)


def deactivate_passenger_api(api_request, api_validator, passenger_id):
    response = api_request.deactivate_passenger_api(passenger_id)
    api_validator.validate_object_deactivated(response)


@pytest.mark.orders
def test_add_order(driver, api_request, api_validator):
    payer_data = add_payer_api(api_request, api_validator)
    passenger_data = add_passenger_api(api_request, api_validator)
    add_order_page = AddOrder(driver, payer_data, passenger_data)
    driver.maximize_window()
    add_order_page.open_add_new_order_form()
    add_order_page.create_new_order()
    search_response = add_order_page.get_search_response_for_new_order(payer_data['account_id'], add_order_page.get_pickup_date())
    api_validator.validate_response_count(search_response)
    deactivate_payer_api(api_request, api_validator, payer_data['id'])
    deactivate_passenger_api(api_request, api_validator, passenger_data['id'])
