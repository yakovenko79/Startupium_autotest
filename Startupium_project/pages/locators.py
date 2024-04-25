from selenium.webdriver.common.by import By

header_tabs = {
    "proj": "Проекты",
    "user": "Пользователи",
    "article": "Статьи",
    "about": "О сайте"
}


class MainPageLocators():
    HEADER_NEW = (By.CSS_SELECTOR, 'section h2')
    TEXT_BTN_PROFILES = (By.XPATH, '//ul/li[text()="Профили"]')
    TITLE = (By.CSS_SELECTOR, "section > h1")
    DESCRIPTION = (By.XPATH, '//main//section/h2')
    LOGIN_LINK = (By.CSS_SELECTOR,
                  "#__next > div.css-1c4mae2 > header > div > "
                  "a.MuiTypography-root.MuiTypography-inherit.MuiLink-root.MuiLink-underlineAlways.css-mss1w8 > span")
    CREATE_CREW_BUTTON = (By.XPATH, '//*[@id="__next"]/div[2]/main/section[1]/div/a[1]')
    LIST_LINKS_CARDS = (By.CSS_SELECTOR, "div >div > div > a[href]")


class LoginPageLocators():
    LOGIN_EMAIL = (By.XPATH, '//input[@placeholder="Введите email"]')
    LOGIN_PASSWORD = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/div/form/ul/li[2]/div/div/div[2]/div/input')
    LOGIN_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/div/form/button')


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
    TAG_CONFIRM = (By.CSS_SELECTOR, "#__next > div.css-1c4mae2 > main > div > div > div > form "
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
    SEARCH_PROJECT_TITLE = (By.XPATH, '//span[text()="Поиск проектов"]')


class HeaderLocators:
    LOGIN_BTN = (By.XPATH, '//header//a[@title="Войти"]')
    HEADER = (By.TAG_NAME, 'header')
    HEADER_PROJECTS_TAB = (By.XPATH, '//header//a[text()="Проекты"]')
    HEADER_USERS_TAB = (By.XPATH, '//header//a[text()="Пользователи"]')
    HEADER_ABOUT_TAB = (By.XPATH, '//header//a[text()="О сайте"]')
    HEADER_ARTICLE_TAB = (By.XPATH, '//a[text()="Статьи"]')
    LOGO_STARTUPIUM = (By.CSS_SELECTOR, 'a')

    @staticmethod
    def get_header_tab(n):
        tab = (By.XPATH, f'//header//a[text()="{header_tabs.get(n)}"]')
        return tab

    @staticmethod
    def get_header_tab_after_click(n):
        tab = (
            By.XPATH, f'//header//a[text()="{header_tabs.get(n)}" and contains (@style, "color: rgb(25, 73, 165);")]')
        return tab


class FooterLocators:
    PRIVACY = (By.CSS_SELECTOR, 'footer div:last-child')
    FOOTER_FOOTER = (By.CSS_SELECTOR, "footer")
    USERS_TAB = (By.CSS_SELECTOR, 'footer li:nth-child(2) > a')
    FEEDBACK = (By.XPATH, "//a[text()='Отзывы и предложения']")
    FEEDBACK_FORM_HEADER = (By.XPATH, "//span[text()='Отзывы и предложения']")
    FEEDBACK_FORM_TITLE = (By.XPATH, '//h3[text()="Помогите нам стать лучше"]')
    FEEDBACK_FORM_FIELD = (By.XPATH, '//*[@id=":r4:"]')
    PROJECTS_TAB = (By.XPATH, '//footer//a[text()="Проекты"]')
    ABOUT_TAB = (By.XPATH, '//footer//a[text()="О сайте"]')


class RegisterPageLocators:
    CHECKBOX_SOCIAL = (By.XPATH, '//main/div/div/div[2]/div[1]/div/div[3]/div/div[1]/div[2]/span[1]/span[1]/input')
    CHECKBOX_ABOUT = (By.XPATH, '//main/div/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/span[1]/span[1]/input')
    CHECKBOX_QUALIFIERS = (By.XPATH, "//main/div/div/div[2]/div[1]/div/div[1]/div/div/div[1]/div[2]/div/span[1]/span[1]/input")
    POSITION_FIELD = (By.CSS_SELECTOR, "input#\:rb\:")
    ROLE_TAG_FOUNDER= (By.XPATH, "//label[@for='founder']")
    NEXT_STEP_BTN = (By.XPATH, "//*[@id='__next']/div[2]/main/div/div/div[2]/div[2]/div[2]/button")
    CHECKBOX_FILL_LATER = (By.XPATH, "//input[@type='checkbox']")
    CHECKBOX_FILL_LATER_2 = (By.XPATH, "//div//span//span//input[@type='checkbox']")


