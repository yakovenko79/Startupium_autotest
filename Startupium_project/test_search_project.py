import time

from Startupium_project.pages.main_page import MainPage
from Startupium_project.pages.search_project import SearchProject

LINK = "https://test.startupium.ru"
EMAIL_USER = "test@te.st"
EMAIL_PASSWORD = "Test123!"
NAME = 'Created from autotest'
DESCRIPTION = 'This is a autotest project'
TAG = 'test-project'
ABOUT = 'This is about testing'
HIRE = "I don't need a human"


class TestSearchProject:
    def test_search_project_unauthorized_user(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        search_project = SearchProject(browser, browser.current_url)
        search_project.go_to_find_project_page()
        search_project.should_be_search_project_url()
        search_project.search_project_by_name(NAME)
        search_project.should_be_search_project_card(NAME)
        search_project.go_to_project_pressing_the_card(NAME)
        search_project.is_title_correct(NAME)



