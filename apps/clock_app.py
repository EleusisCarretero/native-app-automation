from enum import Enum
from apps.base_app import BaseApp
from utils.locators import CamaraLocators, ClockLocators
from utils.scroll import Scroll, ScrollDirection, ScrollError


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
    """ClockApp error class"""

class ClockApp(BaseApp):
    """
    Class to control Clock native application
    """

    def add_new_alarm(self):
        """
        Method to create a new alarm by clicking on plus button
        """
        self.click_app_button(ClockLocators.get_add_new_alarm_locator())

    def scroll_alarm(self, value, which_column):
        """
        Method to scroll down or up in the new alarm window, being able to edit the hour, minute or PM/AM columns

        Args:
            value(str): Hour, minute, or AM/PM value to set the column.
            which_column(AlarmColum): identifier for the desired column to scroll. 
        """
        found_element = None
        if which_column != AlarmColum.MERIDIAN:
            alarm_columns = self.get_list_of_elements(ClockLocators.get_alarm_columns_locator())
            found_element = self.scrolling(
                looking_element=alarm_columns[which_column],
                locator=ClockLocators.get_hours_element_locator(hour_or_minute=value, column=AlarmColum(which_column).name.title()),
                direction=self.chose_direction(time_value=value, column_time=which_column),
            )
        else:
            meridian_column = self.get_list_of_elements(ClockLocators.get_meridian_locator())[0]
            meridian_locator = ClockLocators.get_sub_meridian_locator()
            for direction in [ScrollDirection.UP.value, ScrollDirection.DOWN.value]:
                try:
                    found_element = self.scrolling(
                        looking_element=meridian_column,
                        locator=meridian_locator,
                        max_scrolls=2,
                        direction=direction,
                        specific_text=value)
                    break
                except ClockAppError:
                    print(f"Unable to found the desired element by {direction}")
        if found_element:
            return found_element.text
        raise ClockAppError("Unable to found element")

    def scrolling(self, looking_element, locator, max_scrolls=60, direction=ScrollDirection.DOWN.value, specific_text=""):
        """
        Method to scrolling in the current clock screen.

        Args:
            looking_element (): App element to look for the desired value and scrolling
            locator(tuple): Couple of values to look for the desired element
            max_scrolls(int): number of max scrolls until stop if the element hasn't been found
            direction(ScrollDirection): direction of scroll, up or down
        
        Raises:
            ScrollError: element not found after scrolling
        """
        try:
            return Scroll.scroll_until(
                    looking_element=looking_element,
                    driver=self.base_driver,
                    locator=locator,
                    max_scrolls=max_scrolls,
                    direction=direction,
                    percent=0.3,
                    specific_text=specific_text)
        except ScrollError as e:
            raise ClockAppError("Unable to scroll element until the desired conditions") from e

    def set_week_day(self, day_of_week):
        """
        Method to click on the week day, ina new alarm settings

        Args:
            day_of_week(WeekDays): week day

        Raises:
            ClockAppError: Not valid week day
        """
        if not isinstance(day_of_week, WeekDays):
            raise ClockAppError("Not a valid week day")
        week_day_locator = ClockLocators.get_week_day_locator(day_of_week=day_of_week.value)
        self.click_app_button(week_day_locator)

    def is_week_day_checked(self, day_of_week):
        """
        Method to get the current check value of the 'checkbox' week day

        Args:
            day_of_week(WeekDays): week day

        Returns:
            bool: current check status
        """
        week_day_locator = ClockLocators.get_week_day_locator(day_of_week=day_of_week.value)
        return self.get_check_button_status(week_day_locator)

    @staticmethod
    def chose_direction(time_value, column_time):
        """
        Method to returns the expected scroll direction according to what is faster to take.

        Args:
            time_value(str): Time value, hours or minute
            column_time(AlarmColum): position of the column, hour or minute

        Returns:
            ScrollDirection: better scroll direction
        
        Raises:
            ClockAppError: If the column_time is not a valid option inside of AlarmColum
        """
        if column_time == AlarmColum.HOUR:
            return ScrollDirection.UP.value if int(time_value) < 6 else ScrollDirection.DOWN.value
        elif column_time == AlarmColum.MINUTE:
            return ScrollDirection.UP.value if int(time_value) > 30 else ScrollDirection.DOWN.value
        else:
            raise ClockAppError("Not valid option")

    def write_alarm_name(self, alarm_name):
        """
        Method to write alarm name in the new alarm settings

        Args:
            alarm_name(str): Name of the new alarm
        """
        self.write_text_on_object(ClockLocators.get_alarm_name_locator(), alarm_name)
    
    def read_alarm_name(self):
        """
        Method to read the current alarm name

        Returns:
            str: current alarm name
        """
        return self.get_text(ClockLocators.get_alarm_name_locator())
    
    def save_alarm(self):
        """
        Save the new alarm
        """
        self.click_app_button(ClockLocators.get_save_alarm_locator())

    def get_alarm_list(self):
        """
        Get all the list of current alarms saved

        Returns:
            list: list of current alarms
        """
        return self.get_list_of_elements(ClockLocators.get_alarms_list_locator())
    
    def click_on_alarm(self, alarm):
        """
        Click on the specif alarm
        """
        alarm.click()
