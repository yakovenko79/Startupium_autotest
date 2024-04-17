import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from Startupium_project.pages.base_page import BasePage


class SearchUser(BasePage):
    def should_be_search_user_page_url(self):
        WebDriverWait(self.browser, 10).until(ec.presence_of_element_located((By.XPATH, '//h1[text()="Поиск пользователей"]')))
        assert "users" in self.browser.current_url, "you're not on search user page"

