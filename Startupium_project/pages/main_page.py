from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # def is_this_main_page(self):
    #     assert "https://test.startupium.ru" == self.browser.current_url, "This is not a main page"



