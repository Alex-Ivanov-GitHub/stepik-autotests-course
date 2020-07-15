import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="Chrome",
                     help="Choose browser: Chrome or Firefox")
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose site language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    if browser_name == "Chrome":
        print("\nstart Chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)
    elif browser_name == "Firefox":
        print("\nstart Firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(10)
    else:
        raise pytest.UsageError("--browser should be Chrome or Firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

# Помимо того, что вы рассказывали в вебинаре, та же строка 'browser = None' присутствует в уроке 4.8 шаг 6 пример файла
# conftest.py. Возможно у вас это было нужно из-за того, что browser был объявлен как глобальная переменная.
# Хотелось бы разобрать этот вопрос более подробно.
