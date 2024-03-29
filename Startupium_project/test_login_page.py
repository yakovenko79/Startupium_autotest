import time

import pytest

from Startupium_project.pages.main_page import MainPage
from Startupium_project.pages.login_page import LoginPage

EMAIL_USER = "test@te.st"
EMAIL_PASSWORD = "Test123!"

link = "https://test.startupium.ru"


class TestLoginPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = MainPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()

    def test_login_using_valid_data(self, browser):
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.input_login_credentials(EMAIL_USER, EMAIL_PASSWORD)
        login_page.should_be_login_url()



