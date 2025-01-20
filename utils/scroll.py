import time

from appium.webdriver.common.appiumby import AppiumBy

from utils.zoom import MobileCommands


class Scroll:
    SCROLL_STEP = MobileCommands(f"scrollGesture", elementId='{id}', direction='{direction}', percent='{percent}')

    @classmethod
    def _scrolling(cls, driver, **kwargs):
        driver.execute_script(
            *cls.SCROLL_STEP.command(**kwargs)
        )

    @classmethod
    def scroll_until(cls, looking_element, driver, locator, timeout=10, direction="down", percent=0.3):

        start_time = time.time()
        while time.time() < start_time + timeout:
            try:
                # found_element = looking_element.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.sec.android.app.clockpackage:id/numberpicker_input' and @text='7, Hour']")
                found_element = looking_element.find_element(*locator)
                break
            except:
                # element has not been found yet
                cls._scrolling(driver=driver,id=looking_element.id, direction=direction, percent=percent)
        else:
            print("The element hasn't been found")
        print(f"Element found {found_element}")
