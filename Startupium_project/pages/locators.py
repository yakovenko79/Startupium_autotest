from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,
                  "#__next > div.css-1c4mae2 > header > div > "
                  "a.MuiTypography-root.MuiTypography-inherit.MuiLink-root.MuiLink-underlineAlways.css-mss1w8 > span")
    CREATE_CREW_BUTTON = (By.XPATH, '//*[@id="__next"]/div[2]/main/section[1]/div/a[1]')


class LoginPageLocators():
    LOGIN_EMAIL = (By.XPATH, '//input[@placeholder="Введите email"]')
    LOGIN_PASSWORD = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/div/form/ul/li[2]/div/div/div[2]/div/input')
    LOGIN_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/div/form/button')
    # REGISTER_NAME = (By.CSS_SELECTOR, "input")
    # REGISTER_EMAIL = (By.ID, ":r9:")
    # REGISTER_BUTTON = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div/div/form/button/p')
    # REGISTER_PASSWORD = (By.CSS_SELECTOR, "#\:ra\:")
    # REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#\:rb\:")
    # IS_LOGGED_IN = (By.XPATH, '/html/body/div[1]/div[2]/header/div/div/div[2]/div[1]/button/svg')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,
                  "#__next > div.css-1c4mae2 > header > div > "
                  "a.MuiTypography-root.MuiTypography-inherit.MuiLink-root.MuiLink-underlineAlways.css-mss1w8 > span")
    CREATE_ACCOUNT_LINK = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div/div/div/a[2]/span')


class CreateNewProjectLocators():
    PROJECT_NAME = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/form/div[1]/ul/li[1]/div/div/div/input')
    COUNTRIES_DROP = (By.ID, ':r7:')
    COUNTRY_NAME = (By.ID, ':r7:-option-2')
    CITIES_DROP = (By.ID, ':r9:')
    CITY_NAME = (By.ID, ':r9:-option-5')
    SAVE_TO_DRAFT_BTN = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/form/div[2]/button[2]')
    PUBLISH_PROJECT_BTN = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/form/div[2]/button[1]')
    BRIEF_DESCRIPTION = (By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div/form/div[1]/ul/li[3]/div[2]/div/div"
                                   "/textarea[1]")
    TAGS = (By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div/form/div[1]/ul/li[4]/div/div/div[2]/div["
                      "2]/div/div/input")
    TAG_CONFIRM = (By.CSS_SELECTOR,"#__next > div.css-1c4mae2 > main > div > div > div > form "
                                                           "> div.MuiBox-root.css-1d5z6v1 > ul > li:nth-child(4) > "
                                                           "div > div > div.MuiBox-root.css-1atepvb > "
                                                           "div.MuiAutocomplete-root.MuiAutocomplete-hasPopupIcon.css"
                                                           "-1g2f1u6 > div > div > div > span")
    ABOUT_PROJECT = (By.CSS_SELECTOR, "#__next > div.css-1c4mae2 > main > div > div > div > form > "
                                                 "div.MuiBox-root.css-1d5z6v1 > ul > li:nth-child(5) > "
                                                 "div.MuiBox-root.css-0 > div > div.ql-container.ql-snow > "
                                                 "div.ql-editor.ql-blank > p")
    HIRE_TO_PROJECT = (By.ID, ":rf:")
    HIRE_TO_PROJECT_CONFIRM = (By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div/form/div["
                                                             "1]/ul/li[6]/div/div/div[2]/div["
                                                             "2]/div/div/div/span/button")
    SEE_THE_PROJECT_BTN = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/form/div[2]/div/div/a')
    PROJECT_TITLE = (By.CSS_SELECTOR, 'h2:nth-child(2)')
    NAME_PROJECT_CARD = (By.XPATH, '/html/body/div[1]/div[2]/main/section[2]/div/div[2]/div/div[1]/a/div/div/div['
                                   '1]/div/h2')


class SearchProjectLocators():
    SEARCH_PROJECT_BTN = (By.XPATH, "/html/body/div[1]/div[2]/main/section[1]/div/a[2]")
    SEARCH_PROJECT_FIELD = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/form/div/div[2]/div[1]/div/div/div/input')
    SEARCH_BY_CHECKBOXES = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/form/div/div[3]/div[1]/div[1]/div/div')
    SEARCH_BY_NAME_CHECKBOX = (By.XPATH, '/html/body/div[3]/div[3]/ul/li[2]/span[1]/input')
    SEARCH_SUBMIT = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/form/div/div[2]/div/div/button')
    STRANGE_CLOSE_LIST_CHECKBOX = (By.XPATH, '/html/body/div[3]/div[1]')
    HEADER_H2 = (By.CSS_SELECTOR, 'h2')

# class ProjectCardData():
#     PROJECT_PAGE_CARD_NAME
#     PROJECT_PAGE_CARD_COMMENTS


class HeaderLocators:
    LOGO_STARTUPIUM = (By.CSS_SELECTOR, 'a')


class FooterLocators:
    FEEDBACK = (By.XPATH, "//a[text()='Отзывы и предложения']")
    FEEDBACK_FORM_HEADER = (By.XPATH, "//span[text()='Отзывы и предложения']")
    FEEDBACK_FORM_TITLE = (By.XPATH, '//h3[text()="Помогите нам стать лучше"]')
    FEEDBACK_FORM_FIELD = (By.XPATH, '//*[@id=":r4:"]')
    PROJECTS_TAB = (By.XPATH, '//footer//a[text()="Проекты"]')










