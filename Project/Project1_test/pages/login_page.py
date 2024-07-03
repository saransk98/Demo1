from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.XPATH, '//*[@data-test="error"]')

    def login(self, username, password):
        self.fill_form(*self.USERNAME_FIELD, username)
        self.fill_form(*self.PASSWORD_FIELD, password)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(*self.ERROR_MESSAGE).text
