from wsgiref.util import request_uri

from appium.webdriver.common.appiumby import AppiumBy

class CalculatorLocators:
    BASED_BTTN_XPATH = "//android.widget.Button[@content-desc='{button}']"
    RESULT_ID = "com.sec.android.app.popupcalculator:id/calc_edt_formula"
    @classmethod
    def get_num_locator(cls, num):
        return (AppiumBy.XPATH, cls.BASED_BTTN_XPATH.format(button=num))

    @classmethod
    def get_op_locator(cls, op):
        return (AppiumBy.XPATH, cls.BASED_BTTN_XPATH.format(button=op))
    
    @classmethod
    def get_result(cls):
        return (AppiumBy.ID, cls.RESULT_ID)

class CamaraLocators:
    BASE_ID_BTTNS = "com.sec.android.app.camera:id/{button}"
    @classmethod
    def get_take_picture_locator(cls):
        return (AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="bottom_background"))

    @classmethod
    def get_quick_view_locator(cls):
        return (AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="quick_view_button_layout"))

    @classmethod
    def get_video_locator(cls):
        return (AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="shooting_mode_item_button"))

    @classmethod
    def get_switch_camera_locator(cls):
        return (AppiumBy.ID,cls.BASE_ID_BTTNS.format(button="switch_camera_button"))

class GalleryLocators:

    @classmethod
    def get_info_locator(cls):
        return 	(AppiumBy.XPATH, "(//android.widget.RelativeLayout[@resource-id='com.sec.android.gallery3d:id/img_layout'])[3]")

    @classmethod
    def get_basic_info_locator(cls):
        return (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.sec.android.gallery3d:id/bold_value']")
