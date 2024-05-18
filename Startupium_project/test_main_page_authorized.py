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
