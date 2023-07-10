import unittest

import pytest

from tests.fixtures import driver, add_vehicle_page, api_validator


@pytest.mark.vehicles
# Create new vehicle via UI with only required fields
# Send rest API search request to validate that vehicle was created
def test_add_vehicle(add_vehicle_page, api_validator):
    add_vehicle_page.open_add_new_vehicle_form()
    vehicle_id = add_vehicle_page.create_new_vehicle()
    response = add_vehicle_page.get_search_response_for_new_vehicle(vehicle_id)
    api_validator.validate_response_count(response)
