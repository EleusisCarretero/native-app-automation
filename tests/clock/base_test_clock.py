from apps.clock_app import ClockApp
from tests.base_test import BaseTest



class BaseTestClock(BaseTest):
    def setup(self, driver):
        super().setup(driver)
        self.clock_iface = ClockApp(self.driver_manager.driver)