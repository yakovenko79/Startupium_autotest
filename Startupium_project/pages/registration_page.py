from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Startupium_project.pages.base_page import BasePage
from Startupium_project.pages.locators import RegisterPageLocators
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage(BasePage):
    def input_data_position_field(self):
        position = self.browser.find_element(*RegisterPageLocators.POSITION_FIELD)
        position.send_keys('test position')

    def select_role_by_tag(self):
        role_tag = self.browser.find_element(*RegisterPageLocators.ROLE_TAG_FOUNDER)
        role_tag.click()

    def press_btn_next(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div[2]/main/div/div/div[2]/div[2]/div[2]/button"))).click()

    def press_chkbx_later(self):
        chkbx_later = self.browser.find_element(*RegisterPageLocators.CHECKBOX_FILL_LATER)
        chkbx_later.click()

    def press_btn_next_2(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='__next']/div[2]/main/div/div/div[2]/div[2]/div[2]/button"))).click()

    def press_chkbx_later_2(self):
        chkbx_later = self.browser.find_element(*RegisterPageLocators.CHECKBOX_FILL_LATER_2)
        chkbx_later.click()

    def press_btn_next_3(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='__next']/div[2]/main/div/div/div[2]/div[2]/div[2]/button"))).click()

    def press_chckbx_qualities(self):
        chkbx_qual = self.browser.find_element(*RegisterPageLocators.CHECKBOX_QUALIFIERS)
        chkbx_qual.click()

    def press_checkbox_about(self):
        chkbx_about = self.browser.find_element(*RegisterPageLocators.CHECKBOX_ABOUT)
        chkbx_about.click()

    def press_chkbx_soc_networks(self):
        chkbx_soc_networks = self.browser.find_element(*RegisterPageLocators.CHECKBOX_SOCIAL)
        chkbx_soc_networks.click()

    def press_btn_finish(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='__next']/div[2]/main/div/div/div[2]/div[2]/div[2]/button"))).click()

