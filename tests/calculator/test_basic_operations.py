import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy


@pytest.fixture(scope="class")
def app_data():
    """
    Define app-specific data (e.g., package and activity).
    """
    return {
        "app_package": "com.sec.android.app.popupcalculator",
        "app_activity": "com.sec.android.app.popupcalculator.Calculator"
    }


class TestBasicOperations:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver_manager = driver
    
    def test_addition(self):
        base_xpath = "//android.widget.Button[@content-desc='{button}']"
        print("wait")
        self.driver_manager.driver.find_element(AppiumBy.XPATH, base_xpath.format(button=9)).click()
        time.sleep(3)
        self.driver_manager.driver.find_element(AppiumBy.XPATH, base_xpath.format(button=7)).click()