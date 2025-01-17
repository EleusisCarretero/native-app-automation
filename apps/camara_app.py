from apps.base_app import BaseApp
from utils.locators import CamaraLocators


class CamaraApp(BaseApp):
    def __init__(self, driver):
        super().__init__(driver)
        self.sequence = None

    def take_picture(self):
        self.click_app_button(CamaraLocators.get_take_picture_locator())

    def see_last_picture(self):
        self.click_app_button((CamaraLocators.get_quick_view_locator()))

    def change_to_video(self):
        self.click_app_button(CamaraLocators.get_video_locator())

    def switch_camera(self):
        self.click_app_button(CamaraLocators.get_switch_camera_locator())

    def zoom_camera(self,  percentage, velocity, expand):
        self.make_zoom(percentage=percentage, velocity=velocity, expand=expand, locator=CamaraLocators.get_camera_screen_locator())

    def stepping_zoom_camera(self, stepping ,percentage, velocity, expand=True):
        self.stepping_zoom(stepping=stepping,percentage=percentage, velocity=velocity, expand=expand, locator=CamaraLocators.get_camera_screen_locator())