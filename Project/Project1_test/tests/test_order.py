import time

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_order_product(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login("standard_user", "secret_sauce")
    inventory_page.sort_products()
    inventory_page.add_lowest_priced_product()
    inventory_page.go_to_cart()
    inventory_page.select_check_out()
    checkout_page.enter_checkout_info("John", "Doe", "123")
    assert checkout_page.verify_total_amount("$8.63")
    checkout_page.finish_checkout()
    assert checkout_page.is_thank_you_header_displayed()

