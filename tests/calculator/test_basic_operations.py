import os
import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy

from apps.calculator_app import CalculatorApp
from utils.tools import YamlManager


@pytest.fixture(scope="class")
def app_data():
    """
    Define app-specific data (e.g., package and activity).
    """
    return YamlManager.get_yaml_file_data("config\config.yaml")["apps"]["calculator"]


class TestBasicOperations:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver_manager = driver
        self.cal_iface = CalculatorApp(self.driver_manager.driver)
    
    def test_addition(self):
        print("wait")
        self.cal_iface.tap_num(9)
        time.sleep(1)
        self.cal_iface.tap_num(1)
        time.sleep(1)
        for digit in self.cal_iface.enter_big_number(8904):
            self.cal_iface.tap_num(digit)
            time.sleep(1)


