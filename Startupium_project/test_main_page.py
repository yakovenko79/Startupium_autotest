import time

from Startupium_project.pages.footer import Footer
from Startupium_project.pages.header import Header
from Startupium_project.pages.locators import HeaderLocators
from Startupium_project.pages.login_page import LoginPage
from Startupium_project.pages.main_page import MainPage
from Startupium_project.pages.project_page import ProjectPage
from Startupium_project.pages.search_page import SearchPage

LINK = "https://test.startupium.ru"
ID_PROJECT = "285"
SLUG = "new-project"
ARTICLE_SLUG = "autotest-article"
USERID = "285"
PROJECT_ID = "69"
PAGES = ["/projects",
         "/users",
         "/articles",
         "/about",
         "/login",
         "/create-account",
         "/terms_of_service",
         "/policy",
         f"/project/{SLUG}",
         f"/profile-blog/{USERID}/articles",
         f'/profile-blog/{USERID}/article/{ARTICLE_SLUG}',
         f"/profile/{USERID}",
         f"/project-blog/{PROJECT_ID}/articles"]



class TestMainPage:
    def test_find_project_page_redirect_329(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        search_page = SearchPage(browser, browser.current_url)
        search_page.go_to_find_project_page()
        search_page.should_be_search_project_url()

    def test_create_project_page_redirect_339(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        project_page = ProjectPage(browser, browser.current_url)
        project_page.go_to_project_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.should_be_login_email()
        login_page.should_be_login_password()

    def test_go_to_main_page_by_click_logo_unauthorized_335(self, browser):
        for endpoint in PAGES:
            address = f'{LINK}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            header = Header(browser, browser.current_url)
            header.press_logo()
            header.is_this_main_page(LINK)

    def test_go_to_feedback_form_from_footer_unauth_347(self, browser):
        for endpoint in PAGES:
            address = f'{LINK}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            footer = Footer(browser, browser.current_url)
            footer.go_to_footer()
            footer.go_to_feedback()
            footer.should_feedback_form_appears()

    def test_go_to_projects_page_from_footer_unauth_344(self, browser):
        for endpoint in PAGES:
            address = f'{LINK}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            footer = Footer(browser, browser.current_url)
            footer.go_to_footer()
            footer.go_to_projects()
            projects = SearchPage(browser, browser.current_url)
            projects.should_be_search_project_url()

