import time

from Startupium_project.pages.base_page import BasePage
from Startupium_project.pages.locators import HeaderLocators


class Header(BasePage):

    # def go_to_main_page_by_click_logo_unauthorized(self, browser, link):
    #     pages = ["/projects", "/users", "/articles", "/about", "/login", "/create-account", "/terms_of_service",
    #              "/policy", "/project/{slug}", "/profile-blog/{userId}/articles", "/profile-blog/{userId}/article/{"
    #                                                                               "slug}", "/profile/{id}",
    #              "/project-blog/{projectId}/articles"]
    #     for endpoint in pages:
    #         address = f'{link}{endpoint}'
    #         page = MainPage(browser, address)
    #         page.open()
    #         logo = self.browser.find_element(*HeaderLocators.LOGO_STARTUPIUM)
    #         logo.click()

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





