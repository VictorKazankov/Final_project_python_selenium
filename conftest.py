import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose site language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    link = change_languages(request)
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()


def change_languages(request):
    language_name = request.config.getoption("language")
    if language_name == 'ru':
        print("\nopen russian page")
        link = 'http://selenium1py.pythonanywhere.com/{}/'.format(language_name)
    elif language_name == 'en-gb':
        print("\nopen english page")
        link = 'http://selenium1py.pythonanywhere.com/{}/'.format(language_name)
    elif language_name == 'es':
        print("\nopen spanish page")
        link = 'http://selenium1py.pythonanywhere.com/{}/'.format(language_name)
    elif language_name == 'fr':
        print("\nopen france page")
        link = 'http://selenium1py.pythonanywhere.com/{}/'.format(language_name)
    elif language_name == 'ar':
        print("\nopen arab page")
        link = 'http://selenium1py.pythonanywhere.com/{}/'.format(language_name)
    elif language_name == 'ca':
        print("\nopen catalana page")
        link = 'http://selenium1py.pythonanywhere.com/{}/'.format(language_name)
    elif language_name == 'cs':
        print("\nopen chesky page")
        link = 'http://selenium1py.pythonanywhere.com/{}/'.format(language_name)
    elif language_name == 'da':
        print("\nopen dansky page")
        link = 'http://selenium1py.pythonanywhere.com/{}/'.format(language_name)
    elif language_name == 'de':
        print("\nopen deutsch page")
        link = 'http://selenium1py.pythonanywhere.com/{}/'.format(language_name)
    elif language_name == 'el':
        print("\nopen greece page")
        link = 'http://selenium1py.pythonanywhere.com/{}/'.format(language_name)
    else:
        raise pytest.UsageError("--language_name should be es,ru,fr or en-gb")
    return link
