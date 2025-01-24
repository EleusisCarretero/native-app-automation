"""
BaseTestCalculator class file
"""
from apps.calculator_app import CalculatorApp
from tests.base_test import BaseTest


class BaseTestCalculator(BaseTest):
    """
    Parent test class for al calculator test classes

    Attributes:
        cal_iface(CalculatorApp): instance of calculator interface.
    """
    def setup(self, driver):
        super().setup(driver=driver)
        self.cal_iface = CalculatorApp(self.driver_manager.driver)
