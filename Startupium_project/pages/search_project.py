import time

from selenium.webdriver.common.by import By

from Startupium_project.pages.base_page import BasePage
from Startupium_project.pages.locators import SearchProjectLocators


def create_url(name):
    res = "-".join(name.lower().split())
    return res


class SearchProject(BasePage):

    def go_to_find_project_page(self):
        find = self.browser.find_element(*SearchProjectLocators.SEARCH_PROJECT_BTN)
        find.click()
        time.sleep(2)

    def should_be_search_project_url(self):
        time.sleep(1)
        assert "projects" in self.browser.current_url, "you're not on search project page"

    def should_be_search_project_card(self, name):
        card_names = self.browser.find_elements(By.TAG_NAME, "h2")
        lst = []
        for c in card_names:
            lst.append(c.text)
        assert name in lst, f"Project with name {name} isn't exist"

    def go_to_project_pressing_the_card(self, name):
        card = self.browser.find_element(By.XPATH, f"//*[text()='{name}']")
        card.click()

    def search_name_project_card(self, name):
        pass

    def search_project_by_name(self, name):
        search = self.browser.find_element(*SearchProjectLocators.SEARCH_PROJECT_FIELD)
        search.send_keys(name)
        choice = self.browser.find_element(*SearchProjectLocators.SEARCH_BY_CHECKBOXES)
        choice.click()
        checkbox_name = self.browser.find_element(*SearchProjectLocators.SEARCH_BY_NAME_CHECKBOX)
        checkbox_name.click()
        strange = self.browser.find_element(*SearchProjectLocators.STRANGE_CLOSE_LIST_CHECKBOX)
        strange.click()
        submit_btn = self.browser.find_element(*SearchProjectLocators.SEARCH_SUBMIT)
        submit_btn.click()
        time.sleep(3)

    def is_title_correct(self, name):
        title = self.browser.find_element(*SearchProjectLocators.HEADER_H2).text
        assert name == title, "Wrong title"








