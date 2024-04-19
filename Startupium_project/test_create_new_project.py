from Startupium_project.conftest import browser
from Startupium_project.pages.main_page import MainPage
from Startupium_project.pages.login_page import LoginPage
from Startupium_project.pages.project_page import ProjectPage

LINK = "https://test.startupium.ru"
EMAIL_USER = "test@te.st"
EMAIL_PASSWORD = "Test123!"
NAME = 'Created from autotest'
DESCRIPTION = 'This is a autotest project'
TAG = 'test-project'
ABOUT = 'This is about testing'
HIRE = "I don't need a human"


class TestCreateNewProject:
    # @pytest.fixture(scope="function", autouse=True)
    # def setup(self, browser):
    #     self.page = MainPage(browser, LINK)
    #     self.page.open()
    #     self.page.go_to_login_page()

    def test_create_new_project_into_draft(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.input_login_credentials(EMAIL_USER, EMAIL_PASSWORD)
        project_page = ProjectPage(browser, browser.current_url)
        project_page.go_to_project_page()
        project_page.go_to_project_page()
        project_page.input_project_data(NAME, DESCRIPTION, TAG, ABOUT, HIRE)
        project_page.save_to_draft()
        project_page.should_be_project_url()
        project_page.is_name_of_project_correct(NAME)

    def test_create_and_publish_new_project(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.input_login_credentials(EMAIL_USER, EMAIL_PASSWORD)
        # if "registration" in browser.current_url:
        #     print("Reg page")
        #     reg_page = RegistrationPage(browser, browser.current_url)
        #     reg_page.input_data_position_field()
        #     reg_page.select_role_by_tag()
        #     reg_page.press_btn_next()
        #     reg_page.press_chkbx_later()
        #     reg_page.press_btn_next_2()
        #     reg_page.press_chkbx_later()
        #     reg_page.press_btn_next_3()
        #     reg_page.press_chckbx_qualities()
        #     reg_page.press_checkbox_about()
        #     reg_page.press_chkbx_soc_networks()
        #     reg_page.press_btn_finish()
        project_page = ProjectPage(browser, browser.current_url)
        project_page.go_to_project_page()
        project_page.go_to_project_page()
        project_page.input_project_data(NAME, DESCRIPTION, TAG, ABOUT, HIRE)
        project_page.publish_project()
        project_page.should_be_project_url()
        project_page.is_name_of_project_correct(NAME)
        page.open()
        project_page.is_name_of_project_present_on_main_page(NAME)





