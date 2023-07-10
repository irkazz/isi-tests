import pytest

from tests.fixtures import driver, add_payer_page, api_validator

@pytest.mark.payers
@pytest.mark.failure
def test_add_payer(add_payer_page, api_validator):
    add_payer_page.open_add_new_payer_form()
    payer_id = add_payer_page.create_new_payer()
    response = add_payer_page.get_search_response_for_new_payer(payer_id)
    api_validator.validate_response_count(response)
