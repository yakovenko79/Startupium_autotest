import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Startupium_project.pages.base_page import BasePage
from Startupium_project.pages.locators import HeaderLocators, ProfilePageLocators
from selenium.webdriver.support import expected_conditions as EC


class Header(BasePage):

    def press_logo(self):
        """Нажать логотип Startupium"""
        logo = self.browser.find_element(*HeaderLocators.LOGO_STARTUPIUM)
        logo.click()
        time.sleep(1)

    def is_this_main_page(self, link):
        """Проверка того, что это главная страница"""
        assert link == self.browser.current_url[:-1], "This is not a main page"

    def press_article_tab(self, tab):
        """Нажать таб Статьи"""
        article_tab = self.browser.find_element(*HeaderLocators.get_header_tab(tab))
        article_tab.click()

    def press_projects_tab(self, tab):
        """Нажать таб Проекты"""
        projects_tab = self.browser.find_element(*HeaderLocators.get_header_tab(tab))
        projects_tab.click()

    def should_project_tab(self):
        """Есть ли таб Проекты"""
        assert self.is_element_present(*HeaderLocators.HEADER_PROJECTS_TAB), "Таба проекты в хедере нет"

    def should_this_tab_change_color_after_click(self, tab):
        """Меняет ли цвет таб после клика на нем"""
        assert self.is_element_present(
            *HeaderLocators.get_header_tab_after_click(tab)), "Don't change color of another tab"

    def press_user_tab(self, tab):
        """Нажать таб Пользователи"""
        user_tab = self.browser.find_element(*HeaderLocators.get_header_tab(tab))
        user_tab.click()

    def press_about_tab(self, tab):
        """Нажать таб О сайте"""
        about_tab = self.browser.find_element(*HeaderLocators.get_header_tab(tab))
        about_tab.click()

    def should_header_present(self):
        """Присутствие хедера"""
        assert self.is_element_present(*HeaderLocators.HEADER), "Header is absent"

    def should_users_tab(self):
        """Присутствие таба Пользователи"""
        assert self.is_element_present(*HeaderLocators.HEADER_USERS_TAB), "Users tab is absent"

    def should_articles_tab(self):
        """Присутствие таба Статьи"""
        assert self.is_element_present(*HeaderLocators.HEADER_ARTICLE_TAB), "Articles tab is absent"

    def should_about_tab(self):
        """Присутствие таба О сайте"""
        assert self.is_element_present(*HeaderLocators.HEADER_ABOUT_TAB), "About tab is absent"

    def should_login_button(self):
        """Присутствие кнопки логина"""
        assert self.is_element_present(*HeaderLocators.LOGIN_BTN), "Login button is absent"

    def is_user_logged_in(self):
        """Проверка того, что пользователь авторизован"""
        # assert self.is_not_element_present(*HeaderLocators.LOGIN_BTN)
        assert self.is_element_present(*HeaderLocators.MESSAGES_BTN)
        assert self.is_element_present(*HeaderLocators.NOTIFICATIONS_BTN)

    def are_not_new_messages(self):
        """Есть ли новые сообщения"""
        assert self.is_element_present(*HeaderLocators.MESSAGES_NOT_EXIST), "User has new message"

    def are_new_messages(self):
        """Нет ли новых сообщений"""
        assert self.is_not_element_present(*HeaderLocators.MESSAGES_NOT_EXIST), "Новые сообщения не получены"

    def logout(self):
        """Логаут"""
        open_dropdown = self.browser.find_element(*HeaderLocators.DROPDOWN_MENU_BTN)
        open_dropdown.click()
        logout = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header div:nth-child(4) div li:nth-child(6)'))
        )
        logout.click()

    def go_to_messages(self):
        """Перейти к сообщениям """
        message_btn = self.browser.find_element(*HeaderLocators.MESSAGES_BTN)
        message_btn.click()
        time.sleep(2)
        user_account = self.browser.find_element(*ProfilePageLocators.USER_ACCOUNT_2)
        user_account.click()
        time.sleep(1)
        close_messages_modal = self.browser.find_element(*HeaderLocators.CLOSE_MODAL)
        close_messages_modal.click()

    def are_new_notifications(self):
        """Есть ли новые уведомления"""
        time.sleep(1)
        assert self.is_not_element_present(*HeaderLocators.NOTIFICATIONS_NOT_EXIST), "Новые уведомления не получены"

    def go_to_new_notifications(self):
        """Перейти к уведомлениям"""
        notification_btn = self.browser.find_element(*HeaderLocators.NOTIFICATIONS_BTN)
        notification_btn.click()

    def is_notification_on_alert(self):
        """Проверка того, что алерт уведомлений содержит сообщение"""
        self.is_element_present(*HeaderLocators.PROFILE_NAME_ON_ALERT)
        self.is_element_present(*HeaderLocators.MESSAGE_ON_ALERT)
        self.is_element_present(*HeaderLocators.REMOVE_ALL_NOTIFICATIONS_ALERT_BTN)
        self.is_element_present(*HeaderLocators.MARK_AS_WRITTEN_ALERT_BTN)

    def mark_as_written_notifications(self):
        """Отметить сообщения как прочитанные"""
        mark_btn = self.browser.find_element(*HeaderLocators.MARK_AS_WRITTEN_ALERT_BTN)
        mark_btn.click()
        self.is_element_present(*HeaderLocators.NOTIFICATIONS_NOT_EXIST), "Остались непрочитанные уведомления"
        self.is_not_element_present(*HeaderLocators.MARK_AS_WRITTEN_ALERT_BTN)

    def remove_all_commetns_in_alert(self):
        """Удаление уведомлений из алерта и проверка, что все удалены"""
        remove_notifications = self.browser.find_element(*HeaderLocators.REMOVE_ALL_NOTIFICATIONS_ALERT_BTN)
        remove_notifications.click()
        self.is_not_element_present(*HeaderLocators.MESSAGE_ON_ALERT)
        assert self.browser.find_element(
            *HeaderLocators.MESSAGE_ON_ALERT_HAVENT_NOTIFICATIONS).text == "Нет новых уведомлений", "Уведомления не удалены"

    def open_action_menu(self):
        """Открытие меню действий"""
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header div:nth-child(4) div button'))
        )
        element.click()
        time.sleep(1)

    def go_to_drafts_from_action_menu(self):
        """переход на страницу черновиков из меню действий"""
        profile = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header div:nth-child(4) div li:nth-child(3)'))
        )
        profile.click()

    def should_this_drafts_page(self):
        """проверка того, что открыта страница черновиков"""
        self.browser.set_page_load_timeout(3)
        assert "/my-drafts" in self.browser.current_url, "Это не страница черновиков"
        assert self.is_element_present(*HeaderLocators.DRAFT_HEADER), "Это не страница черновиков"

    def go_to_profile_from_action_menu(self):
        """переход на страницу профиля из меню действий"""
        profile = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header div:nth-child(4) div li:nth-child(1)'))
        )
        profile.click()

    def should_this_profile_page(self, profile_id):
        """проверка того, что открыта страница профиля"""
        time.sleep(2)
        assert f"profile/{profile_id}" in self.browser.current_url, "Это не страница профиля"

    def go_to_my_projects_from_action_menu(self):
        """переход на страницу мои проекты из меню действий"""
        profile = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header div:nth-child(4) div li:nth-child(2)'))
        )
        profile.click()

    def should_this_projects_page(self):
        """проверка того, что открыта страница проектов пользователя"""
        assert "/my-projects" in self.browser.current_url, "Это не адрес страницы проектов пользователя"
        assert self.is_element_present(*HeaderLocators.I_AM_FOUNDER), "Это не страница проектов пользователя"

    def go_to_favorites_from_action_menu(self):
        """переход на страницу избранное из меню действий"""
        favor = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header div:nth-child(4) div li:nth-child(4)'))
        )
        favor.click()

    def should_this_favorites_page(self):
        """Проверка того, что открыта страница Избранное"""
        assert "/my-bookmarks" in self.browser.current_url, "Это не адрес страницы Избранное"
        assert self.is_element_present(*HeaderLocators.FAVORITES_MAIN_TITLE), 'Это не страница Избранное'

    def logout_from_action_menu(self):
        """Логаут из меню действий"""
        logout = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header div:nth-child(4) div li:nth-child(6)'))
        )
        logout.click()

    def should_this_main_page_unauthorized(self):
        """Проверка того, что открыта главная страница и пользователь неавторизован"""
        time.sleep(1)
        assert "https://test.startupium.ru/" == self.browser.current_url, "This is not a main page"
        assert self.is_element_present(*HeaderLocators.LOGIN_BTN), """Пользователь авторизован"""

    def should_action_menu_presence(self):
        """Проверка того, что кнопка меню действий присутствует"""
        assert self.is_element_present(*HeaderLocators.DROPDOWN_MENU_BTN), "Меню действий отсутствует на странице"

    def should_action_menu_btn_is_absence(self):
        """Проверка того, что кнопка меню действий отсутствует"""
        time.sleep(1)
        assert self.is_not_element_present(*HeaderLocators.DROPDOWN_MENU_BTN), "Меню действий присутствует на странице"

    def should_notification_icon(self):
        """Проверка присутствия иконки уведомлений"""
        assert self.is_element_present(*HeaderLocators.NOTIFICATIONS_BTN), "Иконки уведомлений нет"

    def should_messages_icon(self):
        """Проверка присутствия иконки сообщений"""
        assert self.is_element_present(*HeaderLocators.MESSAGES_BTN), "Иконки сообщений нет"









