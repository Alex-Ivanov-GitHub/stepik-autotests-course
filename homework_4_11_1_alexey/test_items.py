import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_checks_product_page_contains_cart_button(browser):
    browser.get(link)
    time.sleep(30)

    # Находим кнопку
    button = browser.find_element_by_css_selector('#add_to_basket_form button')
    button_text = button.text

    # Печатаем в консоль надпись на кнопке
    print("Button text - ", button_text)

    # Проверяем кнопку
    assert len(button_text) != 0, 'No text button'
