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
        return AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="quick_view_button_layout")

    @classmethod
    def get_video_locator(cls):
        return AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="shooting_mode_item_button")

    @classmethod
    def get_switch_camera_locator(cls):
        return AppiumBy.ID,cls.BASE_ID_BTTNS.format(button="switch_camera_button")

    @classmethod
    def get_camera_screen_locator(cls):
        return AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="camera_preview")

    @classmethod
    def get_pause_locator(cls):
        return AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="pause_button")

    @classmethod
    def get_stop_locator(cls):
        return AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="stop_button")


class GalleryLocators:

    @classmethod
    def get_info_locator(cls):
        return 	(AppiumBy.XPATH, "(//android.widget.RelativeLayout[@resource-id='com.sec.android.gallery3d:id/img_layout'])[3]")

    @classmethod
    def get_basic_info_locator(cls):
        return (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.sec.android.gallery3d:id/bold_value']")

class ClockLocators:
    BASE_CLOCK_LOCATOR = "com.sec.android.app.clockpackage:id/{ele_id}"
    BASE_COLUMN_HOUR = "//android.widget.EditText[@resource-id='com.sec.android.app.clockpackage:id/numberpicker_input' and @text='{hour}, {what}']"
    WEEK_DAY_BASE = "com.sec.android.app.clockpackage:id/repeat_{day_of_week}"
    @classmethod
    def get_add_new_alarm_locator(cls):
        return AppiumBy.ID, cls.BASE_CLOCK_LOCATOR.format(ele_id="menu_alarm_add")

    @classmethod
    def get_hours_column(cls):
        return AppiumBy.ID, cls.BASE_CLOCK_LOCATOR.format(ele_id="sesl_timepicker_hour")

    @classmethod
    def get_mins_column(cls):
        return AppiumBy.ID, cls.BASE_CLOCK_LOCATOR.format(ele_id="sesl_timepicker_minute")

    @classmethod
    def get_picker_column(cls):
        return AppiumBy.XPATH, "//android.widget.NumberPicker"

    @classmethod
    def get_alarm_columns_locator(cls):
        return  AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.sec.android.app.clockpackage:id/sesl_timepicker_hour_minute_layout']/android.widget.NumberPicker"

    @classmethod
    def get_hours_element(cls, hour, what):
        return AppiumBy.XPATH, cls.BASE_COLUMN_HOUR.format(hour=hour, what=what)
    
    @classmethod
    def get_meridian(cls):
        return AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.sec.android.app.clockpackage:id/sesl_timepicker_layout']/android.widget.NumberPicker"
                                
    
    @classmethod
    def get_sub_meridian(cls):
        return AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.sec.android.app.clockpackage:id/numberpicker_input']"
    
    @classmethod
    def get_week_day_locator(cls, day_of_week):
        return AppiumBy.ID, cls.WEEK_DAY_BASE.format(day_of_week=day_of_week)
    
    @classmethod
    def get_alarm_name_locator(cls):
        	return AppiumBy.ID, "com.sec.android.app.clockpackage:id/alarm_name"

    @classmethod
    def get_save_alarm_locator(cls):
        return AppiumBy.ID, "com.sec.android.app.clockpackage:id/menu_done"
    
    @classmethod
    def get_alarms_list_locator(cls):
        return AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.app.clockpackage:id/alarm_list_cardView'])"
    
    # @classmethod
    # def get_alarm_name_locator(cls):
    #     return AppiumBy.ID, "com.sec.android.app.clockpackage:id/alarm_list_alarm_name"

    