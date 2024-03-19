from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#span")
    CREATE_CREW_BUTTON = (By.CSS_SELECTOR, "span:nth-child(2)")


class LoginPageLocators():
    REGISTER_NAME = (By.CSS_SELECTOR, "input")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#\:r9\:")
    REGISTER_BUTTON = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div/div/form/button/p')
    REGISTER_PASSWORD = (By.CSS_SELECTOR,"#\:ra\:")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#\:rb\:")




class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "span")