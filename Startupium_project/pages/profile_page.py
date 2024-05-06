import time

from Startupium_project.pages.base_page import BasePage
from Startupium_project.pages.locators import ProfilePageLocators


class Profile(BasePage):

    def should_this_profile_page(self):
        """Проверка того, что открыта страница юзера"""
        assert "/profile/" in self.browser.current_url, "Это не страница профиля юзера"

    def write_message(self):
        write_message_btn = self.browser.find_element(*ProfilePageLocators.WRITE_MESSAGE_BTN)
        write_message_btn.click()
        user_account = self.browser.find_element(*ProfilePageLocators.USER_ACCOUNT)
        user_account.click()
        textarea = self.browser.find_element(*ProfilePageLocators.TEXTAREA_MESSAGE)
        textarea.send_keys("HALO!")
        time.sleep(2)
        send_message_btn = self.browser.find_element(*ProfilePageLocators.SEND_MESSAGE_BTN)
        send_message_btn.click()


