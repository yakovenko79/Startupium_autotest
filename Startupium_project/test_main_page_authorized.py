import pytest

from Startupium_project.pages.header import Header
from Startupium_project.pages.main_page import MainPage
from Startupium_project.pages.login_page import LoginPage
from Startupium_project.pages.profile_page import Profile
from Startupium_project.pages.project_page import ProjectPage
from Startupium_project.pages.search_project import SearchProject

EMAIL_USER = "test@te.st"
EMAIL_PASSWORD = "Test123!"
EMAIL_USER_2 = "example@ex.le"

link = "https://test.startupium.ru"

# ID_PROJECT = "71"
SLUG = "new-project"
PROJECT_ARTICLE_SLUG = "new-new-project-article"
PROFILE_ARTICLE_SLUG = "new-project-blog-article"
ARTICLE_SLUG = "autotest"
# USERID = "2"
PROJECT_ID = "71"
PROFILE_ID = "3"
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
         f"/profile/{PROFILE_ID}",
         "/new-project",
         "/my-projects",
         "/my-drafts",
         "/my-bookmarks",
         "/account-settings",
         "/password_recovery",
         "/registration",
         "/edit-project",
         f"/project-management/chat?id={PROJECT_ID}",
         f"/project-management/team?id={PROJECT_ID}",
         f"/project-management/wiki?id={PROJECT_ID}",
         f"/project-blog/{PROJECT_ID}/article/{PROJECT_ARTICLE_SLUG}",
         f'/profile-blog/{PROFILE_ID}/article/{PROFILE_ARTICLE_SLUG}',
         f"/project-blog/{PROJECT_ID}/articles",
         f"/profile-blog/{PROFILE_ID}/articles"]


@pytest.mark.authorized
class TestMainPageAuth:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = MainPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()

    def test_get_and_send_message_358(self, browser):
        """Проверка возможности отправки сообщений и получения сообщений"""
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.input_login_credentials(EMAIL_USER, EMAIL_PASSWORD)
        head = Header(browser, browser.current_url)
        head.is_user_logged_in()
        head.are_not_new_messages()
        main_page = MainPage(browser, browser.current_url)
        main_page.go_to_profile_from_card()
        profile_page = Profile(browser, browser.current_url)
        profile_page.should_this_profile_page()
        profile_page.write_message()
        head.logout()
        page = MainPage(browser, browser.current_url)
        page.go_to_login_page()
        login_page.input_login_credentials(EMAIL_USER_2, EMAIL_PASSWORD)
        head.is_user_logged_in()
        head.are_new_messages()
        head.go_to_messages()
        head.are_not_new_messages()

    def test_notification_icon_357(self, browser):
        """Проверка функциональности иконки уведомлений в Header, и очистка модального окна со списком уведомлений"""
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.input_login_credentials(EMAIL_USER_2, EMAIL_PASSWORD)
        head = Header(browser, browser.current_url)
        head.is_user_logged_in()
        main_page = MainPage(browser, browser.current_url)
        main_page.go_to_project_from_card()
        project_page = ProjectPage(browser, browser.current_url)
        project_page.write_comment_about_project()
        head.logout()
        main_page.go_to_login_page()
        login_page.input_login_credentials(EMAIL_USER, EMAIL_PASSWORD)
        head.is_user_logged_in()
        head.are_new_notifications()
        head.go_to_new_notifications()
        head.is_notification_on_alert()
        head.mark_as_written_notifications()
        head.remove_all_commetns_in_alert()

    def test_create_new_project_from_button_main_page_364(self, browser):
        """Проверка перехода на страницу поиска проектов при нажатии на кнопку 'Найти проект' обложки главной
        страницы для авторизованного пользователя"""
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.input_login_credentials(EMAIL_USER, EMAIL_PASSWORD)
        head = Header(browser, browser.current_url)
        head.is_user_logged_in()
        find_project = SearchProject(browser, browser.current_url)
        find_project.go_to_find_project_page()
        find_project.should_be_search_project_url()
        find_project.should_be_search_project_page()

    def test_redirect_to_corresponding_profile_from_card_365(self, browser):
        """Проверка перехода на соответствующую страницу профиля при клике на карточку профиля контента главной
        страницы для авторизованного пользователя"""
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.input_login_credentials(EMAIL_USER, EMAIL_PASSWORD)
        head = Header(browser, browser.current_url)
        head.is_user_logged_in()
        profile_card = MainPage(browser, browser.current_url)
        profile_card.go_to_profile_from_card()
        profile = Profile(browser, browser.current_url)
        profile.should_this_profile_page()
        profile.should_profile_data_correspond_card_data()

    def test_redirect_to_corresponding_project_from_card_366(self, browser):
        """Проверка перехода на соответствующую страницу проекта при клике на карточку проекта контента главной
        страницы для авторизованного пользователя"""
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.input_login_credentials(EMAIL_USER, EMAIL_PASSWORD)
        head = Header(browser, browser.current_url)
        head.is_user_logged_in()
        project_card = MainPage(browser, browser.current_url)
        project_card.go_to_project_from_card_and_compare()

    def test_go_to_main_page_by_click_logo_362(self, browser):
        """Проверка перехода на главную страницу приложения Startupium при клике на логотип Startupium в Header с
        любой страницы приложения авторизованным пользователем."""
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.input_login_credentials(EMAIL_USER, EMAIL_PASSWORD)
        head = Header(browser, browser.current_url)
        head.is_user_logged_in()
        for endpoint in PAGES:
            address = f'{link}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            header = Header(browser, browser.current_url)
            header.press_logo()
            header.is_this_main_page(link)

    def test_open_drafts_page_from_action_menu_369(self, browser):
        """Проверка открытия страницы черновиков пользователя при переходе по ссылке 'Черновики' меню действий в
        Header авторизованным пользователем."""
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.input_login_credentials(EMAIL_USER, EMAIL_PASSWORD)
        head = Header(browser, browser.current_url)
        head.is_user_logged_in()
        head.open_action_menu()
        head.go_to_drafts_from_action_menu()
        head.should_this_drafts_page()

    def test_open_profile_page_from_action_menu_367(self, browser):
        """Проверка открытия страницы профиля при переходе по ссылке 'Профиль' меню действий."""
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.input_login_credentials(EMAIL_USER, EMAIL_PASSWORD)
        head = Header(browser, browser.current_url)
        head.is_user_logged_in()
        head.open_action_menu()
        head.go_to_profile_from_action_menu()
        head.should_this_profile_page(PROFILE_ID)
