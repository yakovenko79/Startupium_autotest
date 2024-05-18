import time

from Startupium_project.pages.base_page import BasePage
from Startupium_project.pages.locators import ProfilePageLocators, MainPageLocators


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

    def should_profile_data_correspond_card_data(self):
        """Проверка соответствия имени карточки пользователя и должности в карточке имени пользователя и должности в
        профиле"""
        profile_name = self.browser.find_element(*ProfilePageLocators.PROFILE_NAME)
        assert profile_name.text == "testtest", "Имя не соответствует"
        profile_job_title = self.browser.find_element(*ProfilePageLocators.PROFILE_JOB_NAME)
        assert profile_job_title.text == "fgfg", "Должность не соответствует"





