from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as ec
from Startupium_project.pages.base_page import BasePage


class About(BasePage):
    def should_be_about_page_url(self):
        WebDriverWait(self.browser, 10).until(ec.presence_of_element_located((By.XPATH, '//h1[text()="Startupium — платформа "]')))
        assert "about" in self.browser.current_url, "you're not on about page"