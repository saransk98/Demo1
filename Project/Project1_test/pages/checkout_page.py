from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    ZIP_CODE_FIELD = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')
    TOTAL_LABEL = (By.CLASS_NAME, 'summary_total_label')
    THANK_YOU_HEADER = (By.CLASS_NAME, 'complete-header')

    def enter_checkout_info(self, first_name, last_name, zip_code):
        self.fill_form(*self.FIRST_NAME_FIELD, first_name)
        self.fill_form(*self.LAST_NAME_FIELD, last_name)
        self.fill_form(*self.ZIP_CODE_FIELD, zip_code)
        self.click(*self.CONTINUE_BUTTON)

    def verify_total_amount(self, amount):
        return amount in self.find_element(*self.TOTAL_LABEL).text

    def finish_checkout(self):
        self.click(*self.FINISH_BUTTON)

    def is_thank_you_header_displayed(self):
        return self.find_element(*self.THANK_YOU_HEADER).is_displayed()
