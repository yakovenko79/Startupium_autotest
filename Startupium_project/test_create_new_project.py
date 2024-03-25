import time

import pytest

from Startupium_project.conftest import browser
from Startupium_project.pages.base_page import BasePage
from Startupium_project.pages.main_page import MainPage
from Startupium_project.pages.login_page import LoginPage
from Startupium_project.pages.project_page import ProjectPage

LINK = "https://test.startupium.ru"
EMAIL_USER = "test@te.st"
EMAIL_PASSWORD = "Test123!"
name = 'Test project'
description = 'This is a test project'
tag = 'test-project'
about = 'This is about testing'
hire = 'Tester'


class TestCreateNewProject:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = MainPage(browser, LINK)
        self.page.open()
        self.page.go_to_login_page()

    def test_create_new_project_into_draft(self, browser):
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.input_login_credentials(EMAIL_USER, EMAIL_PASSWORD)
        login_page.should_be_login_url()
        project_page = ProjectPage(browser, browser.current_url)
        project_page.go_to_project_page()
        project_page.go_to_project_page()
        project_page.input_project_data(name, description, tag, about, hire)
        project_page.save_to_draft()
        project_page.should_be_project_url()

