import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver = './drivers/chromedriver.exe'


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language: en-gb, ru, ar, ca, cs, da, de, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, sk, uk, zh-cn")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(executable_path=chrome_driver, options=options)
    print("\nstart chrome browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()

