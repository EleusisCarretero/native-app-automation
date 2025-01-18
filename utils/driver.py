
from appium.options.android import UiAutomator2Options
from appium import webdriver


class AppiumDriverManagerError(Exception):
    pass


class AppiumDriverManager:
    APPIUM_HOST = 'http://127.0.0.1:4723'

    def __init__(self, app_package, app_activity,noReset=False, device_name="192.168.1.64:5555"):
        """
        TODO
        """
        self.capabilities = {
            "platformName": "Android",
            "deviceName": device_name,
            "automationName": "UiAutomator2",
            "appPackage": app_package,
            "appActivity": app_activity,
            "noReset": noReset
        }
        self.driver = None
        self._options = UiAutomator2Options().load_capabilities(self.capabilities)
    
    @property
    def options(self):
        return self._options
    
    def start_driver(self):
        try:
            self.driver = webdriver.Remote(self.APPIUM_HOST, options=self.options)
        except Exception as e:
            raise AppiumDriverManagerError("Unable to start driver") from e
    
    def stop_driver(self):
        # driver = driver or self.driver
        try:
            self.driver.quit()
        except Exception as e:
            raise AppiumDriverManagerError ("Unable to stop driver") from e

        