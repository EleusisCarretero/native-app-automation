from time import sleep

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from apps.clock_app import AlarmColum, WeekDays
from tests.clock.base_test_clock import BaseTestClock
from utils.tools import YamlManager


@pytest.fixture(scope="class")
def app_data():
    """
    Define app-specific data (e.g., package and activity).
    """
    return YamlManager.get_yaml_file_data("config\config.yaml")["apps"]["clock"]

@pytest.fixture(scope="class")
def appium_settings():
    """

    """
    return ['--port', '4723', '--log-level', 'debug']


class TestAlarm(BaseTestClock):

    @pytest.fixture(autouse=True)
    def setup(self, driver, appium_server):
        super().setup(driver)
        

    @pytest.mark.parametrize(
        ("day","time"),
        [
            ("Monday","7:05 PM"),
            # ("Sunday","3:16 AM")
        ]
    )
    def test_one_time_alarm(self, day, time):
        print(day, time)
        hour, minute, meridian = time[0], time[2:4], time[-2:]
        alarm_name = f"Alarm set on {day} at {time}"
        # 1. Click on add new alarm
        self.clock_iface.add_new_alarm()
        sleep(1)
        # 2. Scroll the hours, minute and meridian
        for column_time, type_column in [(hour, AlarmColum.HOUR), (minute, AlarmColum.MINUTE), (meridian, AlarmColum.MERIDIAN)]:
            what_is_set = self.clock_iface.scroll_alarm(column_time, type_column).split(",")[0]
            assert what_is_set == column_time, "The alarm column hasn't been set correctly"
        # 3. Set week day
        self.clock_iface.set_week_day(day_of_week=WeekDays[day.upper()])
        # 4. Get day is selected?
        assert self.clock_iface.is_week_day_checked(day_of_week=WeekDays[day.upper()])
        # 5. Set name
        self.clock_iface.write_alarm_name(alarm_name)
        sleep(1)
        # 6. Save alarm
        self.clock_iface.save_alarm()
        # 7. Click on last alarm saved
        obj_last_alarm = self.clock_iface.get_alarm_list()[-1]
        self.clock_iface.click_on_alarm(obj_last_alarm)
        # 8. compare name
        assert alarm_name == self.clock_iface.read_alarm_name()
