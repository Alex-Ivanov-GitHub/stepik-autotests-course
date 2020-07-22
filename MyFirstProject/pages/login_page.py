from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'Incorrect login url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not present"

    def register_user(self, email: str, pwd1: str, pwd2: str):
        self.find_element(LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(pwd1)
        self.find_element(LoginPageLocators.REPEAT_PASSWORD_FIELD).send_keys(pwd2)
        self.find_element(LoginPageLocators.REGISTER_BUTTON).click()

    def login_user(self, email: str, pwd1: str):
        self.find_element(LoginPageLocators.EMAIL_FIELD_LOGIN).send_keys(email)
        self.find_element(LoginPageLocators.PASSWORD_FIELD_LOGIN).send_keys(pwd1)
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def go_to_password_reset_page(self):
        self.find_element(LoginPageLocators.FORGOTTEN_PASSWORD).click()

    def send_reset_email(self, email: str):
        self.find_element(LoginPageLocators.EMAIL_FIELD_RESET).send_keys(email)
        self.find_element(LoginPageLocators.SEND_EMAIL_BUTTON).click()

    def check_appearing_message(self, message: str):
        message_text = self.find_element(LoginPageLocators.MESSAGE_TEXT).text
        assert message_text == message, f"The message '{message}' is not presented"

    def check_email_sent_page(self, heading: str):
        sent_page = self.find_element(LoginPageLocators.SENT_PAGE_HEADING).text
        assert sent_page == heading, f"The page '{heading}' is not presented"
