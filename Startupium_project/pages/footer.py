import time

from Startupium_project.pages.base_page import BasePage
from Startupium_project.pages.locators import FooterLocators


class Footer(BasePage):

    def go_to_footer(self):
        feedback = self.browser.find_element(*FooterLocators.FEEDBACK)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", feedback)

    def go_to_feedback(self):
        feedback = self.browser.find_element(*FooterLocators.FEEDBACK)
        time.sleep(1)
        feedback.click()

    def should_feedback_form_appears(self):
        assert self.is_element_present(*FooterLocators.FEEDBACK_FORM_TITLE), "Feedback shouldn't appear"
        assert self.is_element_present(*FooterLocators.FEEDBACK_FORM_HEADER), "Feedback header shouldn't appear"

    def go_to_projects(self):
        time.sleep(1)
        projects = self.browser.find_element(*FooterLocators.PROJECTS_TAB)
        projects.click()

    def go_to_search_user(self):
        time.sleep(1)
        search_user = self.browser.find_element(*FooterLocators.USERS_TAB)
        search_user.click()

    def go_to_about(self):
        time.sleep(1)
        about = self.browser.find_element(*FooterLocators.ABOUT_TAB)
        about.click()

    def should_footer_present(self):
        assert self.is_element_present(*FooterLocators.FOOTER_FOOTER), "Футера нет"

    def should_project_footer_tab(self):
        assert self.is_element_present(*FooterLocators.PROJECTS_TAB), "Таба 'Проекты' нет"

    def should_users_footer_tab(self):
        assert self.is_element_present(*FooterLocators.USERS_TAB), "Таба 'Пользователи' нет"

    def should_about(self):
        assert self.is_element_present(*FooterLocators.ABOUT_TAB), "Таба 'О сайте' нет"

    def should_feedback_tab(self):
        assert self.is_element_present(*FooterLocators.FEEDBACK), "Таба 'Отзывы и предложения' нет"

    def should_privacy_links(self):
        assert self.is_element_present(*FooterLocators.PRIVACY), "Сведений о политике конфиденциальности нет"






