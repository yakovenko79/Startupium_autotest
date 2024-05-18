
import pytest

from Startupium_project.pages.about_page import About
from Startupium_project.pages.articles_page import ArticlesPage
from Startupium_project.pages.footer import Footer
from Startupium_project.pages.header import Header
from Startupium_project.pages.login_page import LoginPage
from Startupium_project.pages.main_page import MainPage
from Startupium_project.pages.project_page import ProjectPage
from Startupium_project.pages.search_project import SearchProject
from Startupium_project.pages.search_user import SearchUser
from Startupium_project.pages import login_page

USER_EMAIL_AUTHORIZATION = "test@te.st"
EMAIL_PASSWORD = "Test123!"
LINK = "https://test.startupium.ru"
GET_URL = "https://test.startupium.ru/api/users"
ID_PROJECT = "285"
SLUG = "new-project"
ARTICLE_SLUG = "autotest-article"
USERID = "285"
PROJECT_ID = "69"
PAGES = ["/",
         "/projects",
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









@pytest.mark.regression
class TestMainPage:

    def test_find_project_page_redirect_329(self, browser, authorization):
        """Проверка перехода на страницу поиска проектов при нажатии на кнопку 'Найти проект' обложки главной
        страницы для неавторизованного пользователя"""
        page = MainPage(browser, LINK)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.go_to_login_page()
        authorization(self)
        search_page = SearchProject(browser, browser.current_url)
        search_page.go_to_find_project_page()
        search_page.should_be_search_project_url()
        search_page.should_be_search_project_page()

    def test_redirect_to_login_page_after_press_create_crew_btn_339(self, browser):
        """Проверка перехода на страницу авторизации при нажатии на кнопку 'Собрать команду' обложки главной страницы
        для неавторизованного пользователя"""
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
            projects = SearchProject(browser, browser.current_url)
            projects.should_be_search_project_url()

    def test_go_to_search_user_from_footer_unauth_345(self, browser):
        for endpoint in PAGES:
            address = f'{LINK}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            footer = Footer(browser, browser.current_url)
            footer.go_to_footer()
            footer.go_to_search_user()
            users = SearchUser(browser, browser.current_url)
            users.should_be_search_user_page_url()

    def test_go_to_articles_page_by_click_article_tab_from_header_unauthorized_333(self, browser):
        for endpoint in PAGES:
            address = f'{LINK}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            header = Header(browser, browser.current_url)
            header.press_article_tab("article")
            header.should_this_tab_change_color_after_click("article")
            article_page = ArticlesPage(browser, browser.current_url)
            article_page.should_be_articles_page_url()

    def test_go_to_search_projects_page_by_click_projects_tab_from_header_unauthorized_331(self, browser):
        for endpoint in PAGES:
            address = f'{LINK}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            header = Header(browser, browser.current_url)
            header.press_projects_tab("proj")
            header.should_this_tab_change_color_after_click("proj")
            projects = SearchProject(browser, browser.current_url)
            projects.should_be_search_project_url()
            projects.should_be_search_project_page()

    def test_go_to_users_page_by_click_users_tab_from_header_unauthorized_332(self, browser):
        for endpoint in PAGES:
            address = f'{LINK}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            header = Header(browser, browser.current_url)
            header.press_user_tab("user")
            header.should_this_tab_change_color_after_click("user")
            users = SearchUser(browser, browser.current_url)
            users.should_be_search_user_page_url()

    def test_go_to_about_page_by_click_about_tab_from_header_unauthorized_334(self, browser):
        for endpoint in PAGES:
            address = f'{LINK}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            header = Header(browser, browser.current_url)
            header.press_about_tab("about")
            header.should_this_tab_change_color_after_click("about")
            about = About(browser, browser.current_url)
            about.should_be_about_page_url()

    def test_go_to_about_from_footer_unauth_346(self, browser):
        for endpoint in PAGES:
            address = f'{LINK}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            footer = Footer(browser, browser.current_url)
            footer.go_to_footer()
            footer.go_to_about()
            about = About(browser, browser.current_url)
            about.should_be_about_page_url()

    def test_description_conforms_requirements_unauth_338(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.description_conforms_requirements()

    def test_title_conforms_requirements_unauth_337(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.title_conforms_requirements()

    def test_header_present_on_each_page_unauth_330(self, browser):
        """Хедер присутствует на всех страницах приложения"""
        for endpoint in PAGES:
            address = f'{LINK}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            header = Header(browser, browser.current_url)
            header.should_header_present()
            header.should_project_tab()
            header.should_users_tab()
            header.should_articles_tab()
            header.should_about_tab()
            header.should_login_button()

    def test_footer_present_on_each_page_unauth_343(self, browser):
        """Футер присутствует на всех страницах приложения"""
        for endpoint in PAGES:
            address = f'{LINK}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            footer = Footer(browser, browser.current_url)
            footer.should_footer_present()
            footer.should_project_footer_tab()
            footer.should_users_footer_tab()
            footer.should_about()
            footer.should_feedback_tab()
            footer.should_privacy_links()

    def test_text_button_profiles_ui_unauth_341(self, browser):
        """Проверка того, что сервер возвращает нам карточки только пользователей,
         их не более 30 и они идут по убыванию id"""
        page = MainPage(browser, LINK)
        page.open()
        page.press_text_btn_profiles()
        page.should_only_profile_cards_ui()

    def test_text_button_profiles_api_unauth_341(self):
        """Проверка того, что сервер возвращает нам карточки только пользователей,
         их не более 30 и они идут по убыванию id"""
        MainPage.should_only_profile_cards_api()

    def test_text_button_profiles_ui_api_unauth_341(self, browser):
        """Проверка того, что заголовок имени каждой карточки пользователя в контенте главной страницы соответствует
        значению 'firstname', 'lastname' соответствующего элемента в полученном json файле"""
        page = MainPage(browser, LINK)
        page.open()
        page.press_text_btn_profiles()
        page.check_profile_name_card_conforms_api_ui()
