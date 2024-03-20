from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators
from .main_page import MainPage


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_email()

    def should_be_login_url(self):
        # реализация проверки на корректный url адрес
        assert "login" in self.browser.current_url, "you're not on login page"

    def should_be_register_url(self):
        # реализация проверки на корректный url адрес
        assert "create-account" in self.browser.current_url, "you're not on register page"

    def should_be_profile_url(self):
        # реализация проверки на корректный url адрес
        assert "profile" in self.browser.browser.current_url, "you're not on profile page"

    def go_to_profile(self):
        self.go_to_login_page()
        redirect_to_profile = self.browser.find_element(By.CSS_SELECTOR,
                                                        "#__next > div.css-1c4mae2 > header > div > div > "
                                                        "div:nth-child(4) > div.MuiBox-root.css-0 > ul > "
                                                        "li:nth-child(1) > a")
        redirect_to_profile.click()

    def should_be_login_email(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL)

    def should_be_logged_in(self):
        assert self.is_element_present(*LoginPageLocators.IS_LOGGED_IN)

    def should_be_login_password(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)

    def input_login_credentials(self, email, password):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(email)
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(password)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
