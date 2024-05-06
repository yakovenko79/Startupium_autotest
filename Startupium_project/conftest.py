import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Startupium_project.pages.locators import LoginPageLocators


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
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


# @pytest.fixture(scope="class")
# def authorization():
#     def _authorization(self):
#         self.element_is_visible(self.LoginPageLocators.LOGIN_EMAIL).send_keys(self.USER_EMAIL_AUTHORIZATION)
#         self.element_is_visible(self.LoginPageLocators.LOGIN_PASSWORD).send_keys(self.EMAIL_PASSWORD)
#         self.element_is_visible(self.LoginPageLocators.LOGIN_BUTTON).click()
#
#     return _authorization
