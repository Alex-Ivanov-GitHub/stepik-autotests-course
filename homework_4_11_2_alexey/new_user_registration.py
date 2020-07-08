import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/ru/"
email = "1234567890+28@gmail.com"
password = "test@test"  # не менее 9 символов

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

def test_registration(browser):
    browser.implicitly_wait(10)
    browser.get(link)

    # Вверху справа стартовой страницы кликаем «Войти или зарегистрироваться»
    button = browser.find_element_by_id("login_link")
    button.click()

    # В разделе «Зарегистрироваться» вводим: email, password и повтотяем password
    input1 = browser.find_element_by_id('id_registration-email')
    input1.send_keys(email)
    input2 = browser.find_element_by_id('id_registration-password1')
    input2.send_keys(password)
    input3 = browser.find_element_by_id('id_registration-password2')
    input3.send_keys(password)

    # Нажимаем кнопку Зарегистрироваться
    button = browser.find_element_by_name("registration_submit")
    button.click()

    # На главной странице проверяем появившееся сообщение "Спасибо за регистрацию!"
    welcome_text_elt = browser.find_element_by_css_selector('#messages .alertinner.wicon')
    welcome_text = welcome_text_elt.text
    assert "Спасибо за регистрацию!" == welcome_text
