"""
BaseTest class file
"""


class BaseTest:
    """
    Very basic parent test class, all test classes inherits from it
    
    Attributes:
        driver_manager(Webdriver): Webdriver instance to manipulate current activity
    """
    def setup(self, driver):
        """Setup method"""
        self.driver_manager = driver


if __name__ == "__main__":
    basetest = BaseTest()
