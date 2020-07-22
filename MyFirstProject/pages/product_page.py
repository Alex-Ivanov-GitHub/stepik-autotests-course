from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

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
