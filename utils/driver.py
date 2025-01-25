"""
AppiumDriverManager class file and relates
"""
from appium.options.android import UiAutomator2Options
from appium import webdriver


class AppiumDriverManagerError(Exception):
    """
    AppiumDriverManager Error
    """


class AppiumDriverManager:
    """
    Class to handle the needed driver settings

    Attributes:
        app_package(str): App package
        app_activity(str): App Activity
        device_name(str): Device name
        kwargs(): Other app settings optionally included
    """
    APPIUM_HOST = 'http://127.0.0.1:4723'

    def __init__(self, app_package, app_activity, device_name="192.168.1.64:5555", **kwargs):
        """
        Initialize the driver with the given app settings
        """
        self.capabilities = {
            "platformName": "Android",
            "deviceName": device_name,
            "automationName": "UiAutomator2",
            "appPackage": app_package,
            "appActivity": app_activity,
        }
        for k, v in kwargs.items():
            self.capabilities[k] = v
        self.driver = None
        self._options = UiAutomator2Options().load_capabilities(self.capabilities)
    
    @property
    def options(self):
        """
        Property 'options'
        """
        return self._options
    
    def start_driver(self):
        """
        Start the set driver
        """
        try:
            self.driver = webdriver.Remote(self.APPIUM_HOST, options=self.options)
        except Exception as e:
            raise AppiumDriverManagerError("Unable to start driver") from e
    
    def stop_driver(self):
        """
        Stop current driver
        """
        try:
            self.driver.quit()
        except Exception as e:
            raise AppiumDriverManagerError ("Unable to stop driver") from e
