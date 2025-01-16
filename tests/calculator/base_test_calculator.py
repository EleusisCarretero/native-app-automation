import pytest
from enum import Enum
from apps.calculator_app import CalculatorApp


class BaseTestCalculator:

    def setup(self, driver):
        self.driver_manager = driver
        self.cal_iface = CalculatorApp(self.driver_manager.driver)