from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self):
        # реализация проверки на корректный url адрес
        assert "login" in self.browser.current_url, "you're not on login page"

    def should_be_register_url(self):
        # реализация проверки на корректный url адрес
        assert "create-account" in self.browser.current_url, "you're not on register page"

    def register_new_user(self, email, password):
        reg_name = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)

