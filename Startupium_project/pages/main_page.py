import time
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators, ProjectPageLocators


def check_decreasing(arr):
    return all([x > y for x, y in zip(arr, arr[1:])])


class MainPage(BasePage):
    # это заглушка на случай, если все функции будут перенесены в другие файлы
    # def __init__(self, *args, **kwargs):
    #     super(MainPage, self).__init__(*args, **kwargs)

    def description_conforms_requirements(self):
        """Проверка соответствия надписи обложки главной страницы требованиям"""
        assert self.browser.find_element(
            *MainPageLocators.DESCRIPTION).text == ("Здесь можно найти команду для стартапа, присоединиться к уже "
                                                    "существующему проекту, найти инвестора и партнёра"), (
            "Description "
            "is "
            "different "
            "or absent")

    def title_conforms_requirements(self):
        """Проверка соответствия заголовка главной страницы требованиям"""
        assert self.browser.find_element(
            *MainPageLocators.TITLE).text == "Startupium", "Заголовок не соответствует требованиям или отсутствует"

    def press_text_btn_profiles(self):
        """Нажатие на текстовую кнопку Профили"""
        hdr = self.browser.find_element(*MainPageLocators.HEADER_NEW)
        tb = self.browser.find_element(*MainPageLocators.TEXT_BTN_PROFILES)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", hdr)
        tb.click()
        time.sleep(1)

    def should_only_profile_cards_ui(self):
        """Проверка того, что на странице отображаются только карточки профилей """
        posts = self.browser.find_elements(*MainPageLocators.LIST_LINKS_CARDS)
        links = [post.get_attribute("href") for post in posts]
        for link in links:
            assert "/project/" not in link, "На странице есть карточки проектов"

    @staticmethod
    def should_only_profile_cards_api():
        """Проверка того, что сервер возвращает нам карточки только пользователей,
         их не более 30 и они идут по убыванию id"""

        url = "https://test.startupium.ru/api/users"
        list_of_ids = []
        response = requests.get(url)
        assert response.status_code == 200, "Неудачно"
        js = response.json()
        data = js.get('data')
        for card in data:
            list_of_ids.append(card.get("id"))
            assert card.get("type") == "user", "Сервер возвращает нам не только карточки пользователей"
        assert len(data) <= 30, "Карточек слишком много"
        assert check_decreasing(list_of_ids) is True, "Карточки не по убыванию"

    def get_name_profile_card_from_ui(self):
        """Получение имен пользователей из карточек на UI"""
        l, i = [], 1
        while True:
            try:
                name = self.browser.find_element(By.XPATH,
                                                 f'//section[2]/div/div[2]/div/div[{i}]/a/div/div[1]/div[2]/span[1]').text
                i += 1
                l.append(name)
            except:
                break
        return l

    def get_name_profile_profile_from_api(self):
        """Получение имен пользователей из карточек в json"""
        url = "https://test.startupium.ru/api/users"
        response = requests.get(url)
        js = response.json()
        l = []
        for i in range(len(js['data'])):
            fname = js['data'][i]['firstname']
            lname = js['data'][i]['lastname']
            name = (str(str(fname) if fname is not None else '') + " " + str(
                str(lname) if lname is not None else "")).rstrip()
            l.append(name)
        return l

    def check_profile_name_card_conforms_api_ui(self):
        """Проверка того, что имена в карточках пользователей идут в том же порядке как и в json"""
        assert self.get_name_profile_card_from_ui() == self.get_name_profile_profile_from_api(), "Не совпадают"

    def go_to_profile_from_card(self):
        """Переход на страницу профиля с карточки профиля главной страницы"""
        profile_card = self.browser.find_element(By.XPATH, "//a[@href='/profile/11']")
        ActionChains(self.browser).move_to_element(profile_card).click().perform()
        time.sleep(2)

    def go_to_project_from_card(self):
        """Переход на страницу проекта с карточки проекта"""
        project_card = self.browser.find_element(By.XPATH, "//a[@href='/project/created-project-from-autotest']")
        ActionChains(self.browser).move_to_element(project_card).click().perform()

    def go_to_project_from_card_testtest(self):
        """Переход на страницу проекта с карточки проекта"""
        project_card = self.browser.find_element(By.XPATH, "//a[@href='/project/created-auto-project']")
        ActionChains(self.browser).move_to_element(project_card).click().perform()

    def go_to_project_from_card_and_compare(self):
        """Переход на страницу проекта и сравнение"""
        amount_comments_in_card = self.browser.find_element(*MainPageLocators.AMOUNT_COMMENTS_IN_CARD).text
        project_card = self.browser.find_element(By.XPATH, "//a[@href='/project/created-from-autotest']")
        ActionChains(self.browser).move_to_element(project_card).click().perform()
        time.sleep(2)
        assert "/project/" in self.browser.current_url, "you're not on project page"
        project_name = self.browser.find_element(*ProjectPageLocators.NAME_PROJECT_CARD)
        amount_comments_in_project = self.browser.find_element(*ProjectPageLocators.AMOUNT_COMMENTS_IN_TITLE).text
        number_of_comments = amount_comments_in_project.split()[0]
        assert project_name.text == "Created from autotest", "Это не то название проекта"
        assert amount_comments_in_card == number_of_comments, "Количество комментариев отличается"

    def open_other_cards(self):
        """Нажатие кнопки смотреть еще"""
        see_else_btn = self.browser.find_element(*MainPageLocators.SEE_ELSE_BTN)
        see_else_btn.click()
        time.sleep(2)

    def go_to_the_project_card(self):
        """Поиск конкретной карточки проекта, если ее нет, то нажимается кнопка смотреть еще"""
        while True:
            if self.is_not_element_present(*MainPageLocators.CREATED_PROJECT_CARD):
                see_else_btn = self.browser.find_element(*MainPageLocators.SEE_ELSE_BTN)
                see_else_btn.click()
                time.sleep(2)
            else:
                break

    def should_increase_amount_profile_cards_after_press_see_else_btn(self):
        """Проверка того, что при нажатии кнопки Смотреть еще количество карточек увеличивается"""
        length = self.get_name_profile_card_from_ui()
        if len(length) == 30 and self.is_element_present(*MainPageLocators.SEE_ELSE_BTN):
            see_else_btn = self.browser.find_element(*MainPageLocators.SEE_ELSE_BTN)
            see_else_btn.click()
        else:
            assert self.is_not_element_present(*MainPageLocators.SEE_ELSE_BTN), ("Карточек меньше или больше 30, "
                                                                                 "кнопка Найти еще отсутствует")
        new_length = self.get_name_profile_card_from_ui()
        assert len(new_length) > 30, "Новые карточки не подгружаются"





