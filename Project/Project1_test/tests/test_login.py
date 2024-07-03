import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert driver.find_element(By.CLASS_NAME, "app_logo")

def test_failed_login(driver):
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")
    assert "Epic sadface: Sorry, this user has been locked out." in login_page.get_error_message()
