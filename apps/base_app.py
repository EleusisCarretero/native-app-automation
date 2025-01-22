"""
Base class file
"""
from utils.scroll import Scroll, ScrollError, ScrollDirection
from utils.zoom import Zoom


class BaseAppError(Exception):
    """BaseApp Exception"""


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
        """
        Method to click on an element from a list of elements

        Args:
            locator (tuple): type of identifier (AppiumID), value to look for (str)
            element(WebDriver): Element to look for it
        """
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
        """
        Method to get the current status form check box

        Args:
            locator(tuple): Couple of values to look for the desired element
        
        Returns:
            bool: Checkbox status
        """
        check_obj = self.base_driver.find_elements(*locator)
        return check_obj[0].is_selected

    def write_text_on_object(self, locator, text):
        """
        Method to write a text in a element

        Args:
            locator(tuple): Couple of values to look for the desired element
            text(str): Text to write in app element
        """
        self.base_driver.find_element(*locator).send_keys(text)

    def scrolling(self, looking_element, locator, max_scrolls=60, direction=ScrollDirection.DOWN.value, specific_text=""):
        """
        Method to scrolling in the current clock screen.

        Args:
            looking_element (): App element to look for the desired value and scrolling
            locator(tuple): Couple of values to look for the desired element
            max_scrolls(int): number of max scrolls until stop if the element hasn't been found
            direction(ScrollDirection): direction of scroll, up or down
        
        Raises:
            ScrollError: element not found after scrolling
        """
        try:
            return Scroll.scroll_until(
                    looking_element=looking_element,
                    driver=self.base_driver,
                    locator=locator,
                    max_scrolls=max_scrolls,
                    direction=direction,
                    percent=0.3,
                    specific_text=specific_text)
        except ScrollError as e:
            raise BaseAppError("Unable to scroll element until the desired conditions") from e
