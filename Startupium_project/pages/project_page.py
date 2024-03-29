import time

from Startupium_project.pages.base_page import BasePage
from Startupium_project.pages.locators import MainPageLocators, CreateNewProjectLocators


class ProjectPage(BasePage):

    def should_be_project_url(self):
        assert "project" in self.browser.current_url, "you're not on project page"

    def go_to_project_page(self):
        btn_create_crew = self.browser.find_element(*MainPageLocators.CREATE_CREW_BUTTON)
        btn_create_crew.click()

    def input_project_data(self, name, description, tag, about, hire):
        project_name = self.browser.find_element(*CreateNewProjectLocators.PROJECT_NAME)
        project_name.send_keys(name)
        countries_drop = self.browser.find_element(*CreateNewProjectLocators.COUNTRIES_DROP)
        countries_drop.click()
        country_name = self.browser.find_element(*CreateNewProjectLocators.COUNTRY_NAME)
        country_name.click()
        cities_drop = self.browser.find_element(*CreateNewProjectLocators.CITIES_DROP)
        cities_drop.click()
        city = self.browser.find_element(*CreateNewProjectLocators.CITY_NAME)
        city.click()
        brief_description_field = self.browser.find_element(*CreateNewProjectLocators.BRIEF_DESCRIPTION)
        brief_description_field.send_keys(description)
        tags = self.browser.find_element(*CreateNewProjectLocators.TAGS)
        tags.send_keys(tag)
        tags_confirmation = self.browser.find_element(*CreateNewProjectLocators.TAG_CONFIRM)
        tags_confirmation.click()
        about_project = self.browser.find_element(*CreateNewProjectLocators.ABOUT_PROJECT)
        # self.browser.execute_script("arguments[0].scrollIntoView(true);", about)
        about_project.send_keys(about)
        hire_in_crew = self.browser.find_element(*CreateNewProjectLocators.HIRE_TO_PROJECT)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", hire_in_crew)
        hire_in_crew.send_keys(hire)

    def save_to_draft(self):
        save_to_draft = self.browser.find_element(*CreateNewProjectLocators.SAVE_TO_DRAFT_BTN)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", save_to_draft)
        time.sleep(2)
        save_to_draft.click()
        see_the_project_button = self.browser.find_element(*CreateNewProjectLocators.SEE_THE_PROJECT_BTN)
        see_the_project_button.click()


    # def is_name_of_project_correct():
    #     assert browser.find_element(*CreateNewProjectLocators, PROJECT_TITLE)
