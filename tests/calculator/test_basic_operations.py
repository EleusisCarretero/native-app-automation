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
    
    def test_simple_addition(self):

        result = self.cal_iface.single_seq_operation(num=87596, operations=["+" for _ in range(5)])
        assert int(result) == (8+7+5+9+6)

    def test_simple_substraction(self):
        result = self.cal_iface.single_seq_operation(num=87596, operations=["-" for _ in range(5)])
        assert int(result) == (8-7-5-9-6)

