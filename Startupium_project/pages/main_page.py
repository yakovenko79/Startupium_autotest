import time
import requests
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators


def check_decreasing(arr):
    return all([x > y for x, y in zip(arr, arr[1:])])


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def description_conforms_requirements(self):
        assert self.browser.find_element(
            *MainPageLocators.DESCRIPTION).text == ("Здесь можно найти команду для стартапа, присоединиться в уже "
                                                    "существующий проект, найти инвестора и партнёра"), ("Description "
                                                                                                         "is "
                                                                                                         "different "
                                                                                                         "or absent")

    def title_conforms_requirements(self):
        assert self.browser.find_element(
            *MainPageLocators.TITLE).text == "Startupium", "Заголовок не соответствует требованиям или отсутствует"

    def press_text_btn_profiles(self):
        tb = self.browser.find_element(*MainPageLocators.TEXT_BTN_PROFILES)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", tb)
        tb.click()
        time.sleep(1)

    def should_only_profile_cards_ui(self):
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
        # print(response.raw)
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
                print("name ui ", name)
                l.append(name)
            except:
                break
        return l

    def get_name_profile_profile_from_api(self):
        """Получение имен пользователей из карточек в json"""

        url = "https://test.startupium.ru/api/users"
        response = requests.get(url)
        js = response.json()
        print(js['data'])
        l = []
        for i in range(len(js['data'])):
            fname = js['data'][i]['firstname']
            lname = js['data'][i]['lastname']
            name = (fname + " " + lname).rstrip()
            print("api name ", name)
            l.append(name)
        return l

    def check_profile_name_card_conforms_api_ui(self):
        """Проверка того, что имена в карточках пользователей идут в том же порядке как и в json"""
        assert self.get_name_profile_card_from_ui() == self.get_name_profile_profile_from_api(), "Не совпадают"
