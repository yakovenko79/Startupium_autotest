import pytest

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import chromedriver_autoinstaller


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    chromedriver_autoinstaller.install()
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(options=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

