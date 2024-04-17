import time

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def description_conforms_requirements(self):
        assert self.browser.find_element(*MainPageLocators.DESCRIPTION).text == "Здесь можно найти команду для стартапа, присоединиться в уже существующий проект, найти инвестора и партнёра", "Description is different or absent"
