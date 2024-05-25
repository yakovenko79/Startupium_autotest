import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Startupium_project.pages.base_page import BasePage
from Startupium_project.pages.locators import FooterLocators
from selenium.webdriver.support import expected_conditions as EC


class Footer(BasePage):

    def go_to_footer(self):
        self.browser.set_page_load_timeout(3)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        print(self.browser.current_url)
        time.sleep(1)

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

    def press_policy(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/policy']"))
        ).click()

    def is_this_policy_page(self):
        assert '/policy' in self.browser.current_url, "Это не адрес страницы политики конфиденциальности Startupium"
        assert self.is_element_present(*FooterLocators.POLICY_STARTUPIUM_TITLE), ("Это не страница политики "
                                                                                  "конфиденциальности Startupium")

    def should_privacy_google_links_present(self):
        assert self.is_element_present(*FooterLocators.PRIVACY_GOOGLE_LINK), ("Ссылка политики конфиденциальности "
                                                                              "google отсутствует на странице")
        assert self.is_element_present(*FooterLocators.TERMS_GOOGLE_LINK), ("Ссылка условий использования Google "
                                                                            "отсутствует на странице")
