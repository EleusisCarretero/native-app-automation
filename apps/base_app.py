"""
Base class file
"""
from utils.zoom import Zoom


class BaseAppError(Exception):
    """
    BaseApp Exception
    """
    pass


class BaseApp:
    """
    Base class to control an app

    Attributes:
        base_driver (WebDriver): Webdriver instance of the current session.
    """
    def __init__(self, driver):
        self.base_driver = driver
    
    def click_app_button(self, locator, driver=None):
        """
        Click on the object that matches the 'locator'

        Args:
            locator (tuple): type of identifier (AppiumID), value to look for (str)
        """
        driver = driver or self.base_driver
        button_obj = self.base_driver.find_element(*locator)
        button_obj.click()

    def click_app_button_in_list(self, locator, element):
        button_obj = self.base_driver.find_elements(*locator)[element]
        button_obj.click()
    
    def get_text(self, locator):
        """
        Gets the text from the element which matches with the locator.

         Args:
            locator (tuple): type of identifier (AppiumID), value to look for (str)

        Returns:
            str: text from the object found
        """
        obj = self.base_driver.find_element(*locator)
        return obj.text

    def get_list_of_elements(self, locator):
        """
        Gets a list of all the elements which matches with the 'locator'

        Args:
            locator (tuple): type of identifier (AppiumID), value to look for (str)

        Returns:
            list: list of object which matched with the locator
        """
        try:
            list_obj = self.base_driver.find_elements(*locator)
        except Exception as e:
            raise BaseAppError(f"Unable to found a list of objects by using the locator {locator}") from e
        return list_obj

    def make_zoom(self, locator, percentage=0.5, velocity=1.0, expand=True):
        """
        Makes zoom in an object, it can ben positive or negative.

         Args:
            locator (Tuple): locator of the element to zooming
            percentage (float): Percentage of zoom
            velocity (float): velocity to perform the zoom
            expand (boolean): flag to indicate the sense of the zooming
        """
        Zoom.make_zoom(
            driver=self.base_driver,
            locator=locator,
            percentage=percentage,
            velocity=velocity,
            expand=expand)

    def stepping_zoom(self, locator, stepping ,percentage, velocity, expand=True, wait_time=0.1):
        """
         Args:
            locator (Tuple): locator of the element to zooming
            stepping (float): value to stepping
            percentage (float): Percentage of zoom
            velocity (float): velocity to perform the zoom
            expand (boolean): flag to indicate the sense of the zooming
            wait_time (float): time in seconds to wait before to the next zoom.

        """
        Zoom.stepping_zoom(
            driver=self.base_driver,
            locator=locator,
            stepping=stepping,
            percentage=percentage,
            velocity=velocity,
            expand=expand,
            wait_time=wait_time)
    
    def get_check_button_status(self, locator):
        check_obj = self.base_driver.find_elements(*locator)
        return check_obj[0].is_selected
    
    def write_text_on_object(self, locator, text):
        self.base_driver.find_element(*locator).send_keys(text)


    # def scrolling(self, direction, start_point, increase):
