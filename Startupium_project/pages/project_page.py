import time
from Startupium_project.pages.base_page import BasePage
from Startupium_project.pages.locators import MainPageLocators, CreateNewProjectLocators, ProjectPageLocators


class ProjectPage(BasePage):

    def should_be_project_url(self):
        """Проверка того, что это страница проекта"""
        time.sleep(2)
        assert "/project/" in self.browser.current_url, "you're not on project page"

    def go_to_project_page(self):
        """Переход на страницу создания проекта"""
        btn_create_crew = self.browser.find_element(*MainPageLocators.CREATE_CREW_BUTTON)
        btn_create_crew.click()

    def input_project_data(self, name, description, tag, about, hire):
        """Заполнение полей создания проекта"""
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
        self.browser.execute_script("arguments[0].scrollIntoView(true);", tags)
        tags.send_keys(tag)
        tags_confirmation = self.browser.find_element(*CreateNewProjectLocators.TAG_CONFIRM)
        tags_confirmation.click()
        about_project = self.browser.find_element(*CreateNewProjectLocators.ABOUT_PROJECT)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", about_project)
        about_project.send_keys(about)
        hire_in_crew = self.browser.find_element(*CreateNewProjectLocators.HIRE_TO_PROJECT)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", hire_in_crew)
        hire_in_crew.send_keys(hire)

    def save_to_draft(self):
        """Сохранение проекта в черновики"""
        save_to_draft = self.browser.find_element(*CreateNewProjectLocators.SAVE_TO_DRAFT_BTN)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", save_to_draft)
        time.sleep(2)
        save_to_draft.click()
        see_the_project_button = self.browser.find_element(*CreateNewProjectLocators.SEE_THE_PROJECT_BTN)
        see_the_project_button.click()

    def publish_project(self):
        """Публикация созданного проекта"""
        publish_project = self.browser.find_element(*CreateNewProjectLocators.PUBLISH_PROJECT_BTN)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", publish_project)
        time.sleep(2)
        publish_project.click()
        see_the_project_button = self.browser.find_element(*CreateNewProjectLocators.SEE_THE_PROJECT_BTN)
        see_the_project_button.click()

    def is_name_of_project_correct(self, name):
        """Проверка того, что название проекта верное"""
        project_title = self.browser.find_element(*CreateNewProjectLocators.PROJECT_TITLE).text
        assert project_title == name

    def is_name_of_project_present_on_main_page(self, name):
        """Проверка того, что название проекта есть на главной странице"""
        self.browser.set_page_load_timeout(5)
        project_title = self.browser.find_element(*CreateNewProjectLocators.NAME_PROJECT_CARD).text
        assert project_title == name, "Takogo proekta net"

    def write_comment_about_project(self):
        """Создание комментария о проекте"""
        comment_field = self.browser.find_element(*ProjectPageLocators.COMMENT_FIELD)
        comment_field.send_keys("New message from me")
        send_key = self.browser.find_element(*ProjectPageLocators.SEND_COMMENT_BTN)
        send_key.click()

    def should_project_data_correspond_card_data(self):
        """Проверка соответствия данных в катрочке прокета данным в проекте"""
        project_name = self.browser.find_element(*ProjectPageLocators.NAME_PROJECT_CARD)
        amount_comments_in_project = self.browser.find_element(*ProjectPageLocators.AMOUNT_COMMENTS_IN_TITLE).text
        number_of_comments = amount_comments_in_project.split()[0]
        assert project_name.text == "Created from autotest", "Это не то название проекта"
        assert amount_comments_in_project == number_of_comments, "Количество комментариев отличается"
