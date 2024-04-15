import time

from selenium.webdriver.support.wait import WebDriverWait

from Startupium_project.pages.base_page import BasePage


class ArticlesPage(BasePage):
    def should_be_articles_page_url(self):
        time.sleep(1)
        assert "articles" in self.browser.current_url, "you're not on articles page"