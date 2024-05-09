import time

from Startupium_project.pages.base_page import BasePage
from Startupium_project.pages.locators import HeaderLocators, ProfilePageLocators


class Header(BasePage):

    def press_logo(self):
        logo = self.browser.find_element(*HeaderLocators.LOGO_STARTUPIUM)
        logo.click()
        time.sleep(3)

    def is_this_main_page(self, link):
        assert link == self.browser.current_url[:-1], "This is not a main page"

    def press_article_tab(self, tab):
        article_tab = self.browser.find_element(*HeaderLocators.get_header_tab(tab))
        article_tab.click()

    def press_projects_tab(self, tab):
        projects_tab = self.browser.find_element(*HeaderLocators.get_header_tab(tab))
        projects_tab.click()

    def should_project_tab(self):
        assert self.is_element_present(*HeaderLocators.HEADER_PROJECTS_TAB)

    def should_this_tab_change_color_after_click(self, tab):
        assert self.is_element_present(*HeaderLocators.get_header_tab_after_click(tab)), "Don't change color of another tab"

    def press_user_tab(self, tab):
        user_tab = self.browser.find_element(*HeaderLocators.get_header_tab(tab))
        user_tab.click()

    def press_about_tab(self, tab):
        about_tab = self.browser.find_element(*HeaderLocators.get_header_tab(tab))
        about_tab.click()

    def should_header_present(self):
        assert self.is_element_present(*HeaderLocators.HEADER), "Header is absent"

    def should_users_tab(self):
        assert self.is_element_present(*HeaderLocators.HEADER_USERS_TAB), "Users tab is absent"

    def should_articles_tab(self):
        assert self.is_element_present(*HeaderLocators.HEADER_ARTICLE_TAB), "Articles tab is absent"

    def should_about_tab(self):
        assert self.is_element_present(*HeaderLocators.HEADER_ABOUT_TAB), "About tab is absent"

    def should_login_button(self):
        assert self.is_element_present(*HeaderLocators.LOGIN_BTN), "Login button is absent"

    def is_user_logged_in(self):
        assert self.is_not_element_present(*HeaderLocators.LOGIN_BTN)
        assert self.is_element_present(*HeaderLocators.MESSAGES_BTN)
        assert self.is_element_present(*HeaderLocators.NOTIFICATIONS_BTN)

    def should_messages_list_is_empty(self):
        pass

    def are_not_new_messages(self):
        assert self.is_element_present(*HeaderLocators.MESSAGES_NOT_EXIST), "User has new message"

    def are_new_messages(self):
        assert self.is_not_element_present(*HeaderLocators.MESSAGES_NOT_EXIST), "Новые сообщения не получены"

    def logout(self):
        open_dropdown = self.browser.find_element(*HeaderLocators.DROPDOWN_MENU_BTN)
        open_dropdown.click()
        logout_btn = self.browser.find_element(*HeaderLocators.LOGOUT_BTN)
        logout_btn.click()

    def go_to_messages(self):
        message_btn = self.browser.find_element(*HeaderLocators.MESSAGES_BTN)
        message_btn.click()
        time.sleep(2)
        user_account = self.browser.find_element(*ProfilePageLocators.USER_ACCOUNT_2)
        user_account.click()
        time.sleep(1)
        close_messages_modal = self.browser.find_element(*HeaderLocators.CLOSE_MODAL)
        close_messages_modal.click()

    def are_new_notifications(self):
        assert self.is_not_element_present(*HeaderLocators.NOTIFICATIONS_NOT_EXIST), "Новые уведомления не получены"

    def go_to_new_notifications(self):
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
        assert self.browser.find_element(*HeaderLocators.MESSAGE_ON_ALERT_HAVENT_NOTIFICATIONS).text == "Нет новых уведомлений", "Уведомления не удалены"








