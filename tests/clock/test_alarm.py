"""
Test alarm file
"""
from datetime import datetime, timezone
from time import sleep
import pytest
from apps.clock_app import AlarmColumn, WeekDays
from tests.clock.base_test_clock import BaseTestClock
from utils.tools import MathUtils, YamlManager


@pytest.fixture(scope="class")
def app_data():
    """
    Define app-specific data (e.g., package and activity).
    """
    return YamlManager.get_yaml_file_data("config\config.yaml")["apps"]["clock"]

@pytest.fixture(scope="class")
def appium_settings():
    """
    TODO: include this setting when appium server starts
    """
    return ['--port', '4723', '--log-level', 'debug']


class TestAlarm(BaseTestClock):
    """
    Test class to evaluate alarm fixture
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver, appium_server):
        super().setup(driver)
        

    @pytest.mark.parametrize(
        ("day","time"),
        [
            ("Monday","7:05 PM"),
            ("Sunday","3:03 AM")
        ]
    )
    def test_one_time_alarm(self, day, time):
        """
        Test case to check that a new alarm has been created correctly, having the right
        day, hour, minute and meridian.

        Args:
            day(str): Day of the week.
            time(str): time to set the alarm ex: 'h:m: meridian'
        """
        self.clock_iface.base_driver.implicitly_wait(2)  #Set global timeout to 2 seconds
        print(day, time)
        # Assign variables
        hour, minute, meridian = time[0], time[2:4], time[-2:]
        alarm_name = f"Alarm set on {day} at {time}"
        # 1. Click on add new alarm
        self.clock_iface.add_new_alarm()
        # 2. Scroll the hours, minute and meridian
        for column_time, type_column in [(hour, AlarmColumn.HOUR), (minute, AlarmColumn.MINUTE), (meridian, AlarmColumn.MERIDIAN)]:
            current_column_time = self.clock_iface.scroll_alarm(column_time, type_column).split(",")[0]
            assert current_column_time == column_time, f"The alarm column {type_column.name} hasn't been set correctly"
        # 3. Set week day
        self.clock_iface.set_week_day(day_of_week=WeekDays[day.upper()])
        # 4. Get day is selected?
        assert self.clock_iface.is_week_day_checked(day_of_week=WeekDays[day.upper()]), "The day hasn't been set"
        # 5. Set name
        self.clock_iface.write_alarm_name(alarm_name)
        # 6. Save alarm
        self.clock_iface.save_alarm()
        # 7. Click on last alarm saved
        pos_alarm = -1 if int(hour) > 6 else 0
        self.clock_iface.click_on_alarm(pos_alarm)
        # 8. Compare the alarm name with the name that used previously to named
        assert alarm_name == self.clock_iface.read_alarm_name(), "The alarm name hasn't been saved with the correct name"

    def test_dismiss_activated_alarm(self):
        self.clock_iface.base_driver.implicitly_wait(2)  #Set global timeout to 1 seconds
        # 1. Read current time
        timestamp =  datetime.now(timezone.utc).timestamp()
        dt_object = datetime.fromtimestamp(timestamp)
        print(f"Current time {dt_object}")
        new_dt_object = MathUtils.increment_current_time(dt_object, 0.2)
        new_time = new_dt_object.strftime("%H:%M")
        _tmp_hour, minute = new_time.split(":")
        hour = str(int(_tmp_hour)) if int(_tmp_hour) < 12 else str(int(_tmp_hour) - 12)
        meridian = "AM" if int(_tmp_hour) < 12 else "PM"
        # 2. New alarm
        self.clock_iface.add_new_alarm()
        # 3. Set the alarm time
        for column_time, type_column in [(hour, AlarmColumn.HOUR), (minute, AlarmColumn.MINUTE), (meridian, AlarmColumn.MERIDIAN)]:
            current_column_time = self.clock_iface.scroll_alarm(column_time, type_column).split(",")[0]
            assert current_column_time == column_time, f"The alarm column {type_column.name} hasn't been set correctly"
        # 4. Save alarm
        self.clock_iface.save_alarm()
        sleep(45)  #TODO: make a calculation based on the start time when the alarm time was set
        # 5. Dismiss alarm TODO: how to be sure that the alarm has been dismissed
        self.clock_iface.dismiss_alarm(max_tries=3)
