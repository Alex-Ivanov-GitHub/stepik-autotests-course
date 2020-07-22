from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from datetime import datetime

link = "http://selenium1py.pythonanywhere.com"
email = f'Test_Email_{datetime.now():%Y-%m-%d_%H-%M-%S}@gmail.com'
email_login = "Test_Email_2020-07-22_19-56-45@gmail.com"
pwd1 = "test@test"
pwd2 = "test@test"


@pytest.mark.need_review_custom_scenarios
def test_user_registrations_check_successful(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_register_form()
    login_page.register_user(email, pwd1, pwd2)
    login_page.check_appearing_message("Thanks for registering!")


@pytest.mark.need_review_custom_scenarios
def test_user_can_login(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()
    login_page.login_user(email_login, pwd1)
    login_page.check_appearing_message("Welcome back")


@pytest.mark.need_review_custom_scenarios
def test_user_can_recovery_password(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()
    login_page.go_to_password_reset_page()
    login_page.send_reset_email(email_login)
    login_page.check_email_sent_page("Email sent")
