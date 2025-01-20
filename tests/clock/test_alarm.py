import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

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
        time.sleep(1)
        is_found = self.clock_iface.scroll_alarm(hour[0])
        print(is_found)
        # whole = self.clock_iface.base_driver.find_elements(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.sec.android.app.clockpackage:id/sesl_timepicker_hour_minute_layout']/android.widget.NumberPicker")
        # hours_column = whole[0]
        # for _ in range(10):  # Máximo 10 intentos
        #     try:
        #         # Busca la opción de la hora deseada
        #
        #         hour_option = hours_column.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.sec.android.app.clockpackage:id/numberpicker_input' and @text='7, Hour']")
        #         print("Hora encontrada y seleccionada.")
        #         break
        #     except:
        #         # Si no se encuentra, realiza un scroll en la columna
        #         params = {
        #             "elementId": hours_column.id,
        #             "direction": "down",
        #             "percent": 0.3
        #         }
        #         self.clock_iface.base_driver.execute_script("mobile: scrollGesture", params)
        # else:
        #     print("No se encontró la hora deseada.")