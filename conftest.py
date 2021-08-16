import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose any language, 'es' ")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()


