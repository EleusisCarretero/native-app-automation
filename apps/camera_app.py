from apps.base_app import BaseApp
from utils.locators import CameraLocators


class CameraApp(BaseApp):
    def __init__(self, driver):
        super().__init__(driver)
        self.sequence = None

    def take_picture(self):
        self.click_app_button(CameraLocators.get_take_picture_locator())

    def see_last_picture(self):
        self.click_app_button((CameraLocators.get_quick_view_locator()))

    def change_to_video(self):
        self.click_app_button_in_list(CameraLocators.get_video_locator(),3)

    def switch_camera(self):
        self.click_app_button(CameraLocators.get_switch_camera_locator())

    def zoom_camera(self,  percentage, velocity, expand):
        self.make_zoom(percentage=percentage, velocity=velocity, expand=expand, locator=CameraLocators.get_camera_screen_locator())

    def stepping_zoom_camera(self, stepping ,percentage, velocity, expand=True):
        self.stepping_zoom(stepping=stepping,percentage=percentage, velocity=velocity, expand=expand, locator=CameraLocators.get_camera_screen_locator())

    def pause_recording(self):
        self.click_app_button(CameraLocators.get_pause_locator())

    def stop_recording(self):
        self.click_app_button(CameraLocators.get_stop_locator())
