from selenium.webdriver.common.by import By

from .base_page import BasePage


class InventoryPage(BasePage):
    SORT_DROPDOWN = (By.CLASS_NAME, 'product_sort_container')
    OPTION_VALUE = (By.XPATH, "//option[@value='lohi']")
    ADD_TO_CART_BUTTON = (By.XPATH, '(//button[text()="Add to cart"])[1]')
    CART_ICON = (By.CLASS_NAME, 'shopping_cart_link')
    CHECK_OUT_BUTTON = (By.CLASS_NAME, "btn_action")

    def sort_products(self):
        self.click(*self.SORT_DROPDOWN)
        self.find_element(*self.OPTION_VALUE).click()

    def add_lowest_priced_product(self):
        self.click(*self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.click(*self.CART_ICON)

    def select_check_out(self):
        self.click(*self.CHECK_OUT_BUTTON)
