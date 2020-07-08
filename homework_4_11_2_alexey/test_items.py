import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_checks_product_page_contains_cart_button(browser):
    browser.get(link)

    # Находим кнопку
    button = browser.find_element_by_css_selector('#add_to_basket_form button')
    button_text = button.text

    # Проверяем кнопку
    assert button, 'Button not found'

    # Печатаем в консоль надпись на кнопке
    print("Button text - ", button_text)
# Привязывать проверку кнопки к тексту на ней плохая идея, если кнопка будет
# присутствовать, но текст будет пустой строкой то len вернет 0 и assert сработает.
