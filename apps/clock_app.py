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
                direction="down",
                percent=0.3)
        else:
            meridian_column = self.get_list_of_elements(ClockLocators.get_meridian())[0]
            found_element = Scroll.scroll_until(
            looking_element=meridian_column,
            driver=self.base_driver,
            locator=ClockLocators.get_sub_meridian(),
            direction="down",
            percent=0.3,
            specific_text=value)
        if found_element:
            return found_element.text
        raise ClockAppError("Unable to found element")

    def set_week_day(self, day_of_week):
        # if day_of_week not in WeekDays.__dict__:
        #     raise ClockAppError("Not a valid week day")
        week_day_locator = ClockLocators.get_week_day_locator(day_of_week=day_of_week.value)
        self.click_app_button(week_day_locator)
