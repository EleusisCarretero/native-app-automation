from enum import Enum
from apps.base_app import BaseApp
from utils.locators import CamaraLocators, ClockLocators
from utils.scroll import Scroll


class AlarmColum(int, Enum):
    HOUR = 0
    MINUTE = 1
    MERIDIAN = 2

class WeekDays(int, Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

class ClockAppError(Exception):
    pass

class ClockApp(BaseApp):
    def __init__(self, driver):
        super().__init__(driver)
        self.sequence = None

    def add_new_alarm(self):
        self.click_app_button(ClockLocators.get_add_new_alarm_locator())

    def scroll_alarm(self, value, which_column):
        found_element = None
        current_text = ""
        if which_column != AlarmColum.MERIDIAN:
            alarm_columns = self.get_list_of_elements(ClockLocators.get_alarm_columns_locator())
            found_element = Scroll.scroll_until(
                looking_element=alarm_columns[which_column],
                driver=self.base_driver,
                locator=ClockLocators.get_hours_element(hour=value, what=AlarmColum(which_column).name.title()),
                direction=self.chose_direction(time_value=value, column_time=which_column),
                percent=0.3)
        else:
            meridian_column = self.get_list_of_elements(ClockLocators.get_meridian())[0]
            try:
                found_element = Scroll.scroll_until(
                looking_element=meridian_column,
                driver=self.base_driver,
                locator=ClockLocators.get_sub_meridian(),
                max_scrolls=2,
                direction="down",
                percent=0.3,
                specific_text=value)
            except:
                try:
                    found_element = Scroll.scroll_until(
                    looking_element=meridian_column,
                    driver=self.base_driver,
                    locator=ClockLocators.get_sub_meridian(),
                    max_scrolls=2,
                    direction="up",
                    percent=0.3,
                    specific_text=value)
                except:
                    raise ClockAppError("Unable to found element")
        if found_element:
            return found_element.text
        raise ClockAppError("Unable to found element")

    def set_week_day(self, day_of_week):
        # if day_of_week not in WeekDays.__dict__:
        #     raise ClockAppError("Not a valid week day")
        week_day_locator = ClockLocators.get_week_day_locator(day_of_week=day_of_week.value)
        self.click_app_button(week_day_locator)
    
    def is_week_day_checked(self, day_of_week):
        week_day_locator = ClockLocators.get_week_day_locator(day_of_week=day_of_week.value)
        return self.get_check_button_status(week_day_locator)

    @staticmethod
    def chose_direction(time_value, column_time):
        if column_time == AlarmColum.HOUR:
            return "up" if int(time_value) < 6 else "down"
        elif column_time == AlarmColum.MINUTE:
            return "up" if int(time_value) > 30 else "down"
        else:
            raise ClockAppError("Not valid option")
    
    def write_alarm_name(self, alarm_name):
        self.write_text_on_object(ClockLocators.get_alarm_name_locator(), alarm_name)
    
    def read_alarm_name(self):
        return self.get_text(ClockLocators.get_alarm_name_locator())
    
    def save_alarm(self):
        self.click_app_button(ClockLocators.get_save_alarm_locator())

    def get_alarm_list(self):
        return self.get_list_of_elements(ClockLocators.get_alarms_list_locator())
    
    def click_on_alarm(self, alarm):
        # self.click_app_button(alarm)
        alarm.click()




