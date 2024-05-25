from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        """Перейти на страницу логина"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_register_page(self):
        """Перейти на страницу регистрации"""
        link = self.browser.find_element(*BasePageLocators.CREATE_ACCOUNT_LINK)
        link.click()

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """Проверка того, что элемент присутствует на странице"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=2):
        """Проверка того, что элемент отсутствует на странице"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False



