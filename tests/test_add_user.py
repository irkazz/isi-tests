import pytest
from tests.fixtures import driver, add_user_page, add_driver_user_page, api_validator


@pytest.mark.users
def test_add_admin_user(add_user_page, api_validator):
    add_user_page.open_add_new_user_form()
    username = add_user_page.create_new_admin_user()
    response = add_user_page.get_search_response_for_new_user(username)
    api_validator.validate_response_count(response)


@pytest.mark.users
def test_add_driver_user(add_user_page, add_driver_user_page, api_validator):
    add_user_page.open_add_new_user_form()
    username = add_driver_user_page.create_new_driver_user()
    response = add_user_page.get_search_response_for_new_user(username)
    api_validator.validate_response_count(response)

