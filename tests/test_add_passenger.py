import time
import unittest

import pytest

from tests.fixtures import driver, add_passenger_page, api_validator
from utils.api_requests import API


@pytest.mark.passengers
def test_add_passenger( add_passenger_page, api_validator):
    add_passenger_page.open_add_new_passenger_form()
    last_name = add_passenger_page.create_new_passenger()
    response = add_passenger_page.get_search_response_for_new_passenger(last_name)
    api_validator.validate_response_count(response)

@pytest.mark.payers
def test_add_passenger_api(api_validator):
    api_req = API()
    # Generate timestamp
    timestamp = str(int(time.time()))
    response = api_req.create_passenger_api(timestamp)
    api_validator.validate_client_created(response, timestamp)