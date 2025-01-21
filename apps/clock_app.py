from enum import Enum
from apps.base_app import BaseApp
from utils.locators import CamaraLocators, ClockLocators
from utils.scroll import Scroll

class AlarmColum(int, Enum):
    HOUR = 0
    MINUTE = 1
    MERIDIAN = 2


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
            locator=meridian_column,
            direction="down",
            percent=0.3,
            specific_text=value)
        if found_element:
            return found_element.text
        raise ClockAppError("Unable to found element")