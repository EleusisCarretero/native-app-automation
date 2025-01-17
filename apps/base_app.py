from utils.zoom import Zoom


class BaseAppError(Exception):
    pass


class BaseApp:
    def __init__(self, driver):
        self.base_driver = driver
    
    def click_app_button(self, locator):
        button_obj = self.base_driver.find_element(*locator)
        button_obj.click()
    
    def get_text(self, locator):
        obj = self.base_driver.find_element(*locator)
        return obj.text

    def get_list_of_elements(self,  locator):
        list_obj = self.base_driver.find_elements(*locator)
        return list_obj

    def make_zoom(self, locator, percentage=0.5, velocity=1.0, expand=True):
        """

        Run appium --use-plugins=gestures

        """
        Zoom.make_zoom(
            driver=self.base_driver,
            locator=locator,
            percentage=percentage,
            velocity=velocity,
            expand=expand)

    def stepping_zoom(self, locator, stepping ,percentage, velocity, expand=True):
        Zoom.stepping_zoom(
            driver=self.base_driver,
            locator=locator,
            stepping=stepping,
            percentage=percentage,
            velocity=velocity,
            expand=expand)

