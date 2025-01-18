from wsgiref.util import request_uri

from apps.base_app import BaseApp
from utils.locators import CamaraLocators, ClockLocators
from utils.scroll import Scroll


class ClockApp(BaseApp):
    def __init__(self, driver):
        super().__init__(driver)
        self.sequence = None

    def add_new_alarm(self):
        self.click_app_button(ClockLocators.get_add_new_alarm_locator())

    def scroll_alarm(self, hour):
        alarm_columns = self.get_list_of_elements(ClockLocators.get_hours_element(hour=hour))
        hour_found = Scroll.scroll_until(driver=alarm_columns[0],locator=ClockLocators.get_hours_element(),direction="down", percent=0.3)
        return  hour_found.text