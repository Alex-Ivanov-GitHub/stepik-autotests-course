from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    REPEAT_PASSWORD_FIELD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    EMAIL_FIELD_LOGIN = (By.ID, "id_login-username")
    PASSWORD_FIELD_LOGIN = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    MESSAGE_TEXT = (By.CSS_SELECTOR, "#messages .alertinner.wicon")
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, "#login_form > p > a")
    EMAIL_FIELD_RESET = (By.ID, "id_email")
    SEND_EMAIL_BUTTON = (By.CSS_SELECTOR, "#password_reset_form button.btn")
    SENT_PAGE_HEADING = (By.TAG_NAME, "h1")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")
    COST_PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    COST_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
