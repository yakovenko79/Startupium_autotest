import pytest

from Startupium_project.pages.about_page import About
from Startupium_project.pages.articles_page import ArticlesPage
from Startupium_project.pages.footer import Footer
from Startupium_project.pages.header import Header
from Startupium_project.pages.main_page import MainPage
from Startupium_project.pages.login_page import LoginPage
from Startupium_project.pages.profile_page import Profile
from Startupium_project.pages.project_page import ProjectPage
from Startupium_project.pages.search_project import SearchProject
from Startupium_project.pages.search_user import SearchUser

EMAIL_USER = ""
EMAIL_PASSWORD = ""
EMAIL_USER_2 = ""

link = "https://{domain}.startupium.ru"

SLUG = "new-project"
PROJECT_ARTICLE_SLUG = "new-new-project-blog"
PROFILE_ARTICLE_SLUG = "new-project-blog-article"
ARTICLE_SLUG = "autotest"
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
         "/password-recovery",
         f"/edit-project?slug={SLUG}",
         f"/project-management/chat?id={PROJECT_ID}",
         f"/project-management/team?id={PROJECT_ID}",
         f"/project-management/wiki?id={PROJECT_ID}",
         f"/project-blog/{PROJECT_ID}/article/{PROJECT_ARTICLE_SLUG}",
         f'/profile-blog/{PROFILE_ID}/article/{PROFILE_ARTICLE_SLUG}',
         f"/project-blog/{PROJECT_ID}/articles",
         f"/profile-blog/{PROFILE_ID}/articles"]


@pytest.mark.authorized
@pytest.mark.regression
class TestMainPageAuth:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = MainPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_be_login_url()
        self.login_page.input_login_credentials(EMAIL_USER, EMAIL_PASSWORD)
        self.head = Header(browser, browser.current_url)
        self.head.is_user_logged_in()

    def test_get_and_send_message_358(self, browser):
        """Проверка возможности отправки сообщений и получения сообщений"""
        head = Header(browser, browser.current_url)
        head.are_not_new_messages()
        main_page = MainPage(browser, browser.current_url)
        main_page.go_to_profile_from_card()
        profile_page = Profile(browser, browser.current_url)
        profile_page.should_this_profile_page()
        profile_page.write_message()
        head.logout()
        page = MainPage(browser, browser.current_url)
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.input_login_credentials(EMAIL_USER_2, EMAIL_PASSWORD)
        head.is_user_logged_in()
        head.are_new_messages()
        head.go_to_messages()
        head.are_not_new_messages()

    def test_notification_icon_357(self, browser):
        """Проверка функциональности иконки уведомлений в Header, и очистка модального окна со списком уведомлений"""
        head = Header(browser, browser.current_url)
        main_page = MainPage(browser, browser.current_url)
        main_page.go_to_project_from_card_testtest()
        project_page = ProjectPage(browser, browser.current_url)
        project_page.write_comment_about_project()
        head.logout()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.input_login_credentials(EMAIL_USER_2, EMAIL_PASSWORD)
        head.is_user_logged_in()
        head.are_new_notifications()
        head.go_to_new_notifications()
        head.is_notification_on_alert()
        head.mark_as_written_notifications()
        head.remove_all_commetns_in_alert()

    def test_create_new_project_from_button_main_page_364(self, browser):
        """Проверка перехода на страницу поиска проектов при нажатии на кнопку 'Найти проект' обложки главной
        страницы для авторизованного пользователя"""
        find_project = SearchProject(browser, browser.current_url)
        find_project.go_to_find_project_page()
        find_project.should_be_search_project_url()
        find_project.should_be_search_project_page()

    def test_redirect_to_corresponding_profile_from_card_365(self, browser):
        """Проверка перехода на соответствующую страницу профиля при клике на карточку профиля контента главной
        страницы для авторизованного пользователя"""
        profile_card = MainPage(browser, browser.current_url)
        profile_card.go_to_profile_from_card()
        profile = Profile(browser, browser.current_url)
        profile.should_this_profile_page()
        profile.should_profile_data_correspond_card_data()

    def test_redirect_to_corresponding_project_from_card_366(self, browser):
        """Проверка перехода на соответствующую страницу проекта при клике на карточку проекта контента главной
        страницы для авторизованного пользователя"""
        main = MainPage(browser, browser.current_url)
        main.go_to_the_project_card()
        project_card = MainPage(browser, browser.current_url)
        project_card.go_to_project_from_card_and_compare()

    def test_go_to_main_page_by_click_logo_362(self, browser):
        """Проверка перехода на главную страницу приложения Startupium при клике на логотип Startupium в Header с
        любой страницы приложения авторизованным пользователем."""
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
        head = Header(browser, browser.current_url)
        head.open_action_menu()
        head.go_to_drafts_from_action_menu()
        head.should_this_drafts_page()

    def test_open_profile_page_from_action_menu_367(self, browser):
        """Проверка открытия страницы профиля при переходе по ссылке 'Профиль' меню действий."""
        head = Header(browser, browser.current_url)
        head.open_action_menu()
        head.go_to_profile_from_action_menu()
        head.should_this_profile_page(PROFILE_ID)

    def test_open_my_projects_page_from_action_menu_368(self, browser):
        """Проверка открытия страницы профиля при переходе по ссылке 'Профиль' меню действий."""
        head = Header(browser, browser.current_url)
        head.open_action_menu()
        head.go_to_my_projects_from_action_menu()
        head.should_this_projects_page()

    def test_go_to_policy_page_by_click_policy_in_footer_374(self, browser):
        """Проверка перехода на главную страницу политики в отношении обработки персональных данных при клике на линк
        Политика конфиденциальности в Footer с любой страницы приложения авторизованным пользователем."""
        for endpoint in PAGES:
            address = f'{link}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            footer = Footer(browser, browser.current_url)
            footer.go_to_footer()
            footer.press_policy()
            footer.is_this_policy_page()

    def test_presence_privacy_and_terms_google_links_on_page_375_376(self, browser):
        """Проверка наличия линков политики конфиденциальности и условий использования Google в Footer с любой
        страницы приложения авторизованным пользователем."""
        for endpoint in PAGES:
            address = f'{link}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            footer = Footer(browser, browser.current_url)
            footer.should_privacy_google_links_present()

    def test_open_my_profile_settings_page_from_action_menu_371(self, browser):
        """Проверка открытия страницы профиля при переходе по ссылке 'Профиль' меню действий."""
        head = Header(browser, browser.current_url)
        head.open_action_menu()
        head.go_to_my_projects_from_action_menu()
        head.should_this_projects_page()

    def test_open_favorites_from_action_menu_370(self, browser):
        """Проверка открытия страницы закладок пользователя при переходе по ссылке 'Избранное' меню действий в
        Header."""
        head = Header(browser, browser.current_url)
        head.open_action_menu()
        head.go_to_favorites_from_action_menu()
        head.should_this_favorites_page()

    def test_logout_from_action_menu_372(self, browser):
        """Проверка логаута при переходе по ссылке 'Выйти' меню действий в
        Header."""
        head = Header(browser, browser.current_url)
        head.open_action_menu()
        head.logout_from_action_menu()
        head.should_this_main_page_unauthorized()

    def test_go_to_feedback_form_from_footer_373(self, browser):
        """Проверка того, что при нажатии на таб Отзывы и предложения в футере открывается форма обратной связи"""
        for endpoint in PAGES:
            address = f'{link}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            footer = Footer(browser, browser.current_url)
            footer.go_to_footer()
            footer.go_to_feedback()
            footer.should_feedback_form_appears()

    def test_go_to_projects_page_from_footer_auth_382(self, browser):
        """Проверка доступности страницы поиска проектов для авторизованного пользователя через таб "Проекты" в
        Footer"""
        for endpoint in PAGES:
            address = f'{link}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            footer = Footer(browser, browser.current_url)
            footer.go_to_footer()
            footer.go_to_projects()
            projects = SearchProject(browser, browser.current_url)
            projects.should_be_search_project_url()

    def test_go_to_search_user_from_footer_auth_383(self, browser):
        """Проверка доступности страницы поиска пользователей для авторизованного пользователя через таб
        "Пользователи" в Footer"""
        for endpoint in PAGES:
            address = f'{link}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            footer = Footer(browser, browser.current_url)
            footer.go_to_footer()
            footer.go_to_search_user()
            users = SearchUser(browser, browser.current_url)
            users.should_be_search_user_page_url()

    def test_go_to_articles_page_by_click_article_tab_from_header_unauthorized_379(self, browser):
        """Проверка доступности страницы "Статьи" для авторизованного пользователя через таб "Статьи"
        горизонтального меню Header"""
        for endpoint in PAGES:
            address = f'{link}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            header = Header(browser, browser.current_url)
            header.press_article_tab("article")
            header.should_this_tab_change_color_after_click("article")
            article_page = ArticlesPage(browser, browser.current_url)
            article_page.should_be_articles_page_url()

    def test_go_to_search_projects_page_by_click_projects_tab_from_header_authorized_377(self, browser):
        """Проверка доступности страницы "Проекты" для авторизованного пользователя через таб "Проекты"
        горизонтального меню Header"""
        for endpoint in PAGES:
            address = f'{link}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            header = Header(browser, browser.current_url)
            header.press_projects_tab("proj")
            header.should_this_tab_change_color_after_click("proj")
            projects = SearchProject(browser, browser.current_url)
            projects.should_be_search_project_url()
            projects.should_be_search_project_page()

    def test_go_to_users_page_by_click_users_tab_from_header_authorized_378(self, browser):
        """Проверка доступности страницы "Пользователи" для авторизованного пользователя через таб "Пользователи"
        горизонтального меню Header"""
        for endpoint in PAGES:
            address = f'{link}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            header = Header(browser, browser.current_url)
            header.press_user_tab("user")
            header.should_this_tab_change_color_after_click("user")
            users = SearchUser(browser, browser.current_url)
            users.should_be_search_user_page_url()

    def test_go_to_about_page_by_click_about_tab_from_header_authorized_380(self, browser):
        """Проверка доступности страницы "О сайте" для авторизованного пользователя через таб "О сайте"
        горизонтального меню Header"""
        for endpoint in PAGES:
            address = f'{link}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            header = Header(browser, browser.current_url)
            header.press_about_tab("about")
            header.should_this_tab_change_color_after_click("about")
            about = About(browser, browser.current_url)
            about.should_be_about_page_url()

    def test_go_to_about_from_footer_auth_384(self, browser):
        """Проверка доступности страницы "О сайте" для авторизованного пользователя через таб "О сайте" в Footer"""
        for endpoint in PAGES:
            address = f'{link}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            footer = Footer(browser, browser.current_url)
            footer.go_to_footer()
            footer.go_to_about()
            about = About(browser, browser.current_url)
            about.should_be_about_page_url()

    def test_action_menu_available_only_authorized_user_381(self, browser):
        """Проверка доступности меню действий в Header только авторизованному пользователю"""
        action_menu = Header(browser, browser.current_url)
        action_menu.should_action_menu_presence()
        action_menu.logout()
        action_menu.should_action_menu_btn_is_absence()

    def test_description_conforms_requirements_auth_388(self, browser):
        """Для авторизованного пользователя: проверка соответствия описания приложения на обложке главной страницы
        приложения требованиям"""
        page = MainPage(browser, browser.current_url)
        page.description_conforms_requirements()

    def test_title_conforms_requirements_unauth_387(self, browser):
        """Для авторизованного пользователя: проверка соответствия заголовка обложки главной страницы приложения
        требованиям"""
        page = MainPage(browser, browser.current_url)
        page.title_conforms_requirements()

    def test_header_present_on_each_page_auth_385(self, browser):
        """Хедер присутствует на всех страницах приложения"""
        for endpoint in PAGES:
            address = f'{link}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            header = Header(browser, browser.current_url)
            header.should_header_present()
            header.should_project_tab()
            header.should_users_tab()
            header.should_articles_tab()
            header.should_about_tab()
            header.should_action_menu_presence()
            header.should_notification_icon()
            header.should_messages_icon()

    def test_footer_present_on_each_page_auth_391(self, browser):
        """Футер присутствует на всех страницах приложения"""
        for endpoint in PAGES:
            address = f'{link}{endpoint}'
            page = MainPage(browser, address)
            page.open()
            footer = Footer(browser, browser.current_url)
            footer.should_footer_present()
            footer.should_project_footer_tab()
            footer.should_users_footer_tab()
            footer.should_about()
            footer.should_feedback_tab()
            footer.should_privacy_links()

    def test_text_button_profiles_ui_auth_389(self, browser):
        """Проверка того, что сервер возвращает нам карточки только пользователей,
         их не более 30 и они идут по убыванию id"""
        page = MainPage(browser, browser.current_url)
        page.press_text_btn_profiles()
        page.should_only_profile_cards_ui()

    def test_text_button_profiles_api_auth_389(self):
        """Проверка того, что сервер возвращает нам карточки только пользователей,
         их не более 30 и они идут по убыванию id"""
        MainPage.should_only_profile_cards_api()

    def test_text_button_profiles_ui_api_auth_389(self, browser):
        """Проверка того, что заголовок имени каждой карточки пользователя в контенте главной страницы соответствует
        значению 'firstname', 'lastname' соответствующего элемента в полученном json файле"""
        page = MainPage(browser, browser.current_url)
        page.press_text_btn_profiles()
        page.check_profile_name_card_conforms_api_ui()

    def test_load_more_profile_cards_if_press_see_else_btn_390(self, browser):
        """Для авторизованного пользователя: Проверка загрузки дополнительных карточек при нажатии на кнопку
        'Смотреть еще' для выбранного фильтра 'Профили'"""
        main = MainPage(browser, browser.current_url)
        main.press_text_btn_profiles()
        main.should_only_profile_cards_ui()
        main.should_increase_amount_profile_cards_after_press_see_else_btn()
