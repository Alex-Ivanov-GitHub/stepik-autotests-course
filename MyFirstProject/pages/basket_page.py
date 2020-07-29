from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.support.ui import Select
from ..constants import FIRST_NAME, LAST_NAME, ADDRESS, CITY, ZIP_CODE, COUNTRY


class BasketPage(BasePage):
    def checkout(self):
        self.proceed_to_checkout()
        self.input_shipping_address()
        self.input_payment_details()
        self.place_order()

    def proceed_to_checkout(self):
        self.find_element(BasketPageLocators.PROCEED_TO_CHECKOUT).click()

    def input_shipping_address(self):
        self.find_element(BasketPageLocators.FIRST_NAME).send_keys(FIRST_NAME)
        self.find_element(BasketPageLocators.LAST_NAME).send_keys(LAST_NAME)
        self.find_element(BasketPageLocators.ADDRESS).send_keys(ADDRESS)
        self.find_element(BasketPageLocators.CITY).send_keys(CITY)
        self.find_element(BasketPageLocators.ZIP_CODE).send_keys(ZIP_CODE)
        Select(self.find_element(BasketPageLocators.COUNTRY)).select_by_visible_text(COUNTRY)
        self.find_element(BasketPageLocators.CONTINUE).click()

    def input_payment_details(self):
        self.find_element(BasketPageLocators.CONTINUE).click()

    def place_order(self):
        self.find_element(BasketPageLocators.PLACE_ORDER).click()

    def should_not_be_items_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "There is an item in the cart, but should not be"

    def should_be_text_message_that_the_cart_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "There is no message that the cart is empty"

    def should_be_confirmation_of_order(self):
        assert "thank-you" in self.browser.current_url, \
            'Order not confirmed, not correct URL'
