import pytest
import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from datetime import datetime
from .constants import BASE_URL, PRODUCT_URL, LOGIN_URL, EMAIL_LOGIN, PASSWORD


@pytest.mark.need_review_custom_scenarios
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LOGIN_URL)
        page.open()
        email = f"{time.time()}@fakemail.org"
        page.register_new_user(email, PASSWORD)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_the_waiting_list(self, browser):
        page = ProductPage(browser, PRODUCT_URL)
        page.open()
        page.add_product_to_wish_list()
        page.should_be_success_message()

    def test_user_can_checkout(self, browser):
        page = ProductPage(browser, PRODUCT_URL)
        page.open()
        page.add_product_to_basket()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.checkout()
        basket_page.should_be_confirmation_of_order()


@pytest.mark.need_review_custom_scenarios
def test_guest_can_register_successfully(browser):
    page = MainPage(browser, BASE_URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_register_form()
    email = f'Test_Email_{datetime.now():%Y-%m-%d_%H-%M-%S}@gmail.com'
    login_page.register_new_user(email, PASSWORD)
    login_page.check_appearing_message("Thanks for registering!")


@pytest.mark.need_review_custom_scenarios
def test_user_can_login(browser):
    page = MainPage(browser, BASE_URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()
    login_page.login_user(EMAIL_LOGIN, PASSWORD)
    login_page.check_appearing_message("Welcome back")


@pytest.mark.need_review_custom_scenarios
def test_user_can_recovery_password(browser):
    page = MainPage(browser, BASE_URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()
    login_page.go_to_password_reset_page()
    login_page.send_reset_email(EMAIL_LOGIN)
    login_page.check_email_sent_page("Email sent")
