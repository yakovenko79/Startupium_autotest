from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,
                  "#__next > div.css-1c4mae2 > header > div > "
                  "a.MuiTypography-root.MuiTypography-inherit.MuiLink-root.MuiLink-underlineAlways.css-mss1w8 > span")
    CREATE_CREW_BUTTON = (By.CSS_SELECTOR, "span:nth-child(2)")


class LoginPageLocators():
    LOGIN_EMAIL = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/div/form/ul/li[1]/div/div/div[2]/div/input')
    LOGIN_PASSWORD = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/div/form/ul/li[2]/div/div/div[2]/div/input')
    LOGIN_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/div/form/button')
    REGISTER_NAME = (By.CSS_SELECTOR, "input")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#\:r9\:")
    REGISTER_BUTTON = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div/div/form/button/p')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#\:ra\:")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#\:rb\:")
    IS_LOGGED_IN = (By.XPATH, '/html/body/div[1]/div[2]/header/div/div/div[2]/div[1]/button/svg')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,
                  "#__next > div.css-1c4mae2 > header > div > "
                  "a.MuiTypography-root.MuiTypography-inherit.MuiLink-root.MuiLink-underlineAlways.css-mss1w8 > span")
    CREATE_ACCOUNT_LINK = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div/div/div/a[2]/span')
