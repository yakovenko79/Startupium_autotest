import time

from Startupium_project.pages.base_page import BasePage
from Startupium_project.pages.locators import HeaderLocators
from Startupium_project.pages.main_page import MainPage


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
        print("link ", link)
        print("browser curr link ", self.browser.current_url)
        print("browser curr link [:-1] ", self.browser.current_url)
        assert link == self.browser.current_url[:-1], "This is not a main page"




