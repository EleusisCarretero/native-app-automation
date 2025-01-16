import time
from apps.base_app import BaseApp
from utils.locators import CamaraLocators


class CamaraApp(BaseApp):
    def __init__(self, driver):
        super().__init__(driver)
        self.sequence = None

    def take_picture(self):
        self.click_app_button(CamaraLocators.get_take_picture_locator())

    def see_last_picture(self):
        time.sleep(0.5)
        self.click_app_button((CamaraLocators.get_quick_view_locator()))

    def change_to_video(self):
        self.click_app_button(CamaraLocators.get_video_locator())

    def switch_camera(self):
        self.click_app_button(CamaraLocators.get_switch_camera_locator())