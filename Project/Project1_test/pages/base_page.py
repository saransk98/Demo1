from selenium.webdriver.common.by import By
from selenium import webdriver
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by: object, value: object) -> object:
        self.find_element(by, value).click()

    def fill_form(self, by, value, text):
        self.find_element(by, value).send_keys(text)
