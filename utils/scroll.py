import time

from utils.zoom import MobileCommands


class Scroll:
    SCROLL_STEP = MobileCommands(f"scrollGesture", elementId='{id}', direction='{direction}', percent='{percent}')

    @classmethod
    def _scrolling(cls, driver, **kwargs):
        driver.execute_script(
            *cls.SCROLL_STEP.command(**kwargs)
        )

    @classmethod
    def scroll_until(cls, driver, locator, timeout=10, direction="down", percent=0.1):

        start_time = time.time()
        while time.time() < start_time + timeout:
            try:
                found_element = driver.find_elemt(*locator)
                return found_element
            except:
                # element has not been found yet
                cls._scrolling(driver=driver,id=id, direction=direction, percent=percent)
        print("The element hasn't been found")
