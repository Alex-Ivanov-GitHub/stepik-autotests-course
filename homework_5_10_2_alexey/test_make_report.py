from datetime import datetime

link = "http://selenium1py.pythonanywhere.com"
email = f'Test_Email_{datetime.now():%Y-%m-%d_%H-%M-%S}@gmail.com'
password = "test@test"  # не менее 9 символов


def test_user_registrations_check_successful(browser):
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

    # На главной странице проверяем появившееся сообщение "Thanks for registering!"
    welcome_text_elt = browser.find_element_by_css_selector('#messages .alertinner.wicon')
    welcome_text = welcome_text_elt.text
    assert welcome_text == "Thanks for registering!", "The registration message is not presented"
