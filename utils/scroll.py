import time

from appium.webdriver.common.appiumby import AppiumBy

from utils.zoom import MobileCommands

class ScrollError(Exception):
    pass

class Scroll:
    SCROLL_STEP = MobileCommands(f"scrollGesture", elementId='{id}', direction='{direction}', percent='{percent}')

    @classmethod
    def _scrolling(cls, driver, **kwargs):
        driver.execute_script(
            *cls.SCROLL_STEP.command(**kwargs)
        )

    @classmethod
    def scroll_until(cls, looking_element, driver, locator, max_scrolls=60, direction="down", percent=0.3, specific_text=""):
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
        
