from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group a.btn-default")


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
    ADD_TO_WISH_LIST_BTN = (By.CLASS_NAME, "btn-wishlist")
    NAME_PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")
    COST_PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    COST_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    PROCEED_TO_CHECKOUT = (By.CLASS_NAME, "btn-primary")
    FIRST_NAME = (By.ID, "id_first_name")
    LAST_NAME = (By.ID, "id_last_name")
    ADDRESS = (By.ID, "id_line1")
    CITY = (By.ID, "id_line4")
    ZIP_CODE = (By.ID, "id_postcode")
    CONTINUE = (By.CLASS_NAME, "btn-lg")
    PLACE_ORDER = (By.ID, "place-order")
    COUNTRY = (By.ID, "id_country")
