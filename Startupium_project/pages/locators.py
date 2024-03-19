from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#span")
    CREATE_CREW_BUTTON = (By.CSS_SELECTOR, "span:nth-child(2)")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,)




class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "span")