import unittest

import pytest

from tests.fixtures import driver, add_passenger_page, api_validator


@pytest.mark.passengers
def test_add_passenger( add_passenger_page, api_validator):
    add_passenger_page.open_add_new_passenger_form()
    last_name = add_passenger_page.create_new_passenger()
    response = add_passenger_page.get_search_response_for_new_passenger(last_name)
    api_validator.validate_response_count(response)

