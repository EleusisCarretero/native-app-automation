
from apps.calculator_app import CalculatorApp
from tests.base_test import BaseTest


class BaseTestCalculator(BaseTest):

    def setup(self, driver):
        # self.driver_manager = driver
        self.cal_iface = CalculatorApp(self.driver_manager.driver)