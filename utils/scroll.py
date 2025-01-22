from enum import Enum
from utils.zoom import MobileCommands


class ScrollDirection(str, Enum):
    """Enum to control scroll direction"""
    UP = "up"
    DOWN = "down"


class ScrollError(Exception):
    """Scroll Error"""


class Scroll:
    """
    Gesture class to scroll in the app screen
    """
    SCROLL_STEP = MobileCommands(f"scrollGesture", elementId='{id}', direction='{direction}', percent='{percent}')

    @classmethod
    def _scrolling(cls, driver, **kwargs):
        driver.execute_script(
            *cls.SCROLL_STEP.command(**kwargs)
        )

    @classmethod
    def scroll_until(cls, looking_element, driver, locator, max_scrolls=60, direction=ScrollDirection.DOWN.value, percent=0.3, specific_text=""):
        """
        Method to scroll a screen until some element has been found, or until the element has the corresponding text.

        Args:
            looking_element (): App element to look for the desired value and scrolling
            driver(WebDriver): Web driver element
            locator(tuple): Couple of values to look for the desired element
            max_scrolls(int): number of max scrolls until stop if the element hasn't been found
            direction(ScrollDirection): direction of scroll, up or down
            percent(float): Percentage to do the scroll in the, previously defined direction
            specific_text(str/Optional): expected text value to found the element, it is optional.

        Returns:
            Webdriver: Element found which covers the conditions
        
        Raises:
            ScrollError: The element haven't been found.
        """
        found_element = None
        count_scroll = 1
        while count_scroll <= max_scrolls:
            try:
                found_element = looking_element.find_element(*locator)
                if specific_text:
                    if specific_text == found_element.text:
                        return found_element
                    raise ScrollError("Continue")
                return found_element
            except:
                cls._scrolling(driver=driver,id=looking_element.id, direction=direction, percent=percent)
            count_scroll += 1
        else:
            print("The element hasn't been found")
        raise ScrollError(f"Not found element")
