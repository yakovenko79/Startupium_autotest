import time

from selenium.webdriver import ActionChains

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







