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
    browser = None
    if browser_name == "Chrome":
        print("\nstart Chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)
    elif browser_name == "Firefox":
        print("\nstart Firefox browser for test..")
        browser = webdriver.Firefox(options=options)
        browser.implicitly_wait(10)
    else:
        raise pytest.UsageError("--browser should be Chrome or Firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
