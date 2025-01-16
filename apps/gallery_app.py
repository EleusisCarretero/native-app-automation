from apps.base_app import BaseApp
from utils.locators import GalleryLocators


class GalleryApp(BaseApp):
    def __init__(self, driver):
        super().__init__(driver)
        self.sequence = None

    def click_info_button(self):
        self.click_app_button(GalleryLocators.get_info_locator())

    def get_picture_date(self):
        obj = self.get_list_of_elements(GalleryLocators.get_basic_info_locator())[0]
        return obj.text