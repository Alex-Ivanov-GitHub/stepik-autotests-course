from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def add_product_to_wish_list(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_WISH_LIST_BTN).click()

    def check_of_product(self):
        name = self.find_element(ProductPageLocators.NAME_PRODUCT).text
        self.check_name_of_product(name)
        cost = self.find_element(ProductPageLocators.COST_PRODUCT).text
        self.check_cost_of_product(cost)

    def check_name_of_product(self, name_product: str):
        name_product_message = self.find_element(ProductPageLocators.NAME_PRODUCT_MESSAGE).text
        assert name_product_message == name_product, "Incorrect name of product"

    def check_cost_of_product(self, cost_product: str):
        cost_product_message = self.find_element(ProductPageLocators.COST_PRODUCT_MESSAGE).text
        assert cost_product_message == cost_product, "Incorrect cost of product"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
