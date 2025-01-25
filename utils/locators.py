"""
Locators file
"""
from appium.webdriver.common.appiumby import AppiumBy


class CalculatorLocators:
    """
    Calculator locator
    """
    BASED_BTTN_XPATH = "//android.widget.Button[@content-desc='{button}']"
    RESULT_ID = "com.sec.android.app.popupcalculator:id/calc_edt_formula"
    @classmethod
    def get_num_locator(cls, num):
        """
        Calculator number locator
    
        Args: num(int): unit number to located

        Returns:
            Tuple: Locator
        """
        return AppiumBy.XPATH, cls.BASED_BTTN_XPATH.format(button=num)

    @classmethod
    def get_op_locator(cls, op):
        """
        Arithmetic operation Locator

        Args: op(str): Arithmetic operation

        Returns:
            Tuple: Locator
        """
        return AppiumBy.XPATH, cls.BASED_BTTN_XPATH.format(button=op)
    
    @classmethod
    def get_result(cls):
        """
        Result Locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID, cls.RESULT_ID

class CameraLocators:
    """
    Camera locators
    """
    BASE_ID_BTTNS = "com.sec.android.app.camera:id/{button}"

    @classmethod
    def get_take_picture_locator(cls):
        """
        Button to take picture locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="bottom_background")

    @classmethod
    def get_quick_view_locator(cls):
        """
        Quick view button locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="quick_view_button_layout")

    @classmethod
    def get_video_locator(cls):
        """
        Button to record video locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="shooting_mode_item_button")

    @classmethod
    def get_switch_camera_locator(cls):
        """
        Switch camera button locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID,cls.BASE_ID_BTTNS.format(button="switch_camera_button")

    @classmethod
    def get_camera_screen_locator(cls):
        """
        Camera screen locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="camera_preview")

    @classmethod
    def get_pause_locator(cls):
        """
        Pause button locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="pause_button")

    @classmethod
    def get_stop_locator(cls):
        """
        Stope button locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID, cls.BASE_ID_BTTNS.format(button="stop_button")


class GalleryLocators:
    """
    Gallery locators
    """

    @classmethod
    def get_info_locator(cls):
        """
        Get info button locator

        Returns:
            Tuple: Locator
        """
        return 	AppiumBy.XPATH, "(//android.widget.RelativeLayout[@resource-id='com.sec.android.gallery3d:id/img_layout'])[3]"

    @classmethod
    def get_basic_info_locator(cls):
        """
        Basic button information locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.sec.android.gallery3d:id/bold_value']"


class ClockLocators:
    """
    Class Clock locators
    """
    # Alarm locators base
    BASE_ID_LOCATOR = "com.sec.android.app.clockpackage:id/"
    BASE_CLOCK_LOCATOR = BASE_ID_LOCATOR + "{ele_id}"
    BASE_COLUMN_HOUR = "//android.widget.EditText[@resource-id='" + BASE_ID_LOCATOR + "numberpicker_input' and @text='{hour_or_minute}, {column}']"
    WEEK_DAY_BASE = BASE_ID_LOCATOR + "repeat_{day_of_week}"

    @classmethod
    def get_add_new_alarm_locator(cls):
        """
        Add alarm button locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID, cls.BASE_CLOCK_LOCATOR.format(ele_id="menu_alarm_add")

    @classmethod
    def get_hours_column_locator(cls):
        """
        Hours column locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID, cls.BASE_CLOCK_LOCATOR.format(ele_id="sesl_timepicker_hour")

    @classmethod
    def get_mins_column_locator(cls):
        """
        Minute column locator
        
        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID, cls.BASE_CLOCK_LOCATOR.format(ele_id="sesl_timepicker_minute")

    @classmethod
    def get_picker_column_locator(cls):
        """
        Picker column locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.XPATH, "//android.widget.NumberPicker"

    @classmethod
    def get_alarm_columns_locator(cls):
        """
        Alarm column locator

        Returns:
            Tuple: Locator
        """
        return  AppiumBy.XPATH, f"//android.widget.LinearLayout[@resource-id='{cls.BASE_CLOCK_LOCATOR.format(ele_id="sesl_timepicker_hour_minute_layout")}']/android.widget.NumberPicker"

    @classmethod
    def get_hours_element_locator(cls, hour_or_minute, column):
        """Hours elment locator

        Args:
            hour_or_minute(str): hour or minute value
            column(str): Column, hour, or minute

        Returns:
            Tuple: Locator
        """
        return AppiumBy.XPATH, cls.BASE_COLUMN_HOUR.format(hour_or_minute=hour_or_minute, column=column)

    @classmethod
    def get_meridian_locator(cls):
        """
        Meridian locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.XPATH, f"//android.widget.LinearLayout[@resource-id='{cls.BASE_CLOCK_LOCATOR.format(ele_id="sesl_timepicker_layout")}']/android.widget.NumberPicker"             

    @classmethod
    def get_sub_meridian_locator(cls):
        """
        Meridian locator sub element

        Returns:
            Tuple: Locator
        """
        return AppiumBy.XPATH, f"//android.widget.TextView[@resource-id='{cls.BASE_CLOCK_LOCATOR.format(ele_id="numberpicker_input")}']"

    @classmethod
    def get_week_day_locator(cls, day_of_week):
        """Week day locator

        Args:
            day_of_week(int): number of the week

        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID, cls.WEEK_DAY_BASE.format(day_of_week=day_of_week)

    @classmethod
    def get_alarm_name_locator(cls):
        """
        Field which has the alarm name

        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID, cls.BASE_CLOCK_LOCATOR.format(ele_id="alarm_name")

    @classmethod
    def get_save_alarm_locator(cls):
        """
        Save alarm button locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.ID, cls.BASE_CLOCK_LOCATOR.format(ele_id="menu_done")

    @classmethod
    def get_alarms_list_locator(cls):
        """
        Saved alarm list locator

        Returns:
            Tuple: Locator
        """
        return AppiumBy.XPATH, f"(//android.widget.FrameLayout[@resource-id='{cls.BASE_CLOCK_LOCATOR.format(ele_id="alarm_list_cardView")}'])"  
