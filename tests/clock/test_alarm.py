import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from apps.clock_app import AlarmColum
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
        ("day","hour"),
        [
            ("Monday","7:30 AM"),
            # ("Friday","5:15 AM"),
            # ("Wednesday","7:30 PM"),
            # ("Sunday","6:16 PM")
        ]
    )
    def test_one_time_alarm(self, day, hour):
        print(day, hour)
        self.clock_iface.add_new_alarm()
        # time.sleep(1)
        # is_found = self.clock_iface.scroll_alarm(hour[0], AlarmColum.HOUR)
        # print(is_found)
        is_found = self.clock_iface.scroll_alarm(hour[2:4], AlarmColum.MINUTE)
        print(is_found)
