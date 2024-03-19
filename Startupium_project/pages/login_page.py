from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self):
        # реализация проверки на корректный url адрес
        assert "login" in self.browser.current_url, "login is not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not on the page"