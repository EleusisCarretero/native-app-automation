import pytest
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
        for column_time, type_column in [(hour, AlarmColum.HOUR), (minute, AlarmColum.MINUTE), (meridian, AlarmColum.MERIDIAN)]:
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
