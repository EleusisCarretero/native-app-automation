"""
BaseTestClock class file
"""
from apps.clock_app import ClockApp
from tests.base_test import BaseTest


class BaseTestClock(BaseTest):
    """
    Paren test class for all test clock classes

    Attribute:
        clock_iface(ClockApp): Instance of app interface.
    """
    def setup(self, driver):
        super().setup(driver)
        self.clock_iface = ClockApp(self.driver_manager.driver)
