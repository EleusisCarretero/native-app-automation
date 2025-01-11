from appium.webdriver.common.appiumby import AppiumBy
class CalculatorLocators:
    BASED_XPATH = "//android.widget.Button[@content-desc='{button}']"
    @classmethod
    def get_num_locator(cls, num):
        return (AppiumBy.XPATH, cls.BASED_XPATH.format(button=num))