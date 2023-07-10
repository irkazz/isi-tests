import pytest

from selenium.webdriver.common.by import By

from tests.fixtures import driver, navigation_page, login_page


@pytest.mark.navigation
def test_navigation(driver, login_page, navigation_page):
    login_page.login()
    assert login_page.wait_for_element_visible((By.CSS_SELECTOR, "img.brand-logo-img"))
    navigation_page.init_page()
    items = navigation_page.get_items()
    for item in items:
        navigation_page.nav_item_click(item)
        if item.is_top_item_with_sub_items():
            for sub_item in item.get_sub_items():
                navigation_page.nav_sub_item_click(sub_item)
                assert navigation_page.is_title_text_changed(sub_item.get_title())
                assert driver.current_url == sub_item.get_url(), f"Assertion failed: Expected {sub_item.get_url()}, " \
                                                                 f"but got {driver.current_url}"
        else:
            assert navigation_page.is_title_text_changed(item.get_title())
            assert driver.current_url == item.get_url(), f"Assertion failed: Expected {item.get_url()}, " \
                                                             f"but got {driver.current_url}"
