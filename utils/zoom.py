import time
from enum import Enum

class MobileCommands(tuple, Enum):
    MOBILE = "mobile"
    ZOOM_AND_EXPAND = (f"{MOBILE}: pinchOpenGesture",
                       "{{'elementId': '{id}', 'percent': {percentage}, 'velocity': {velocity}}}")
    ZOOM_AND_REDUCE = (f"{MOBILE}: pinchCloseGesture",
                       "{{'elementId': '{id}', 'percent': {percentage}, 'velocity': {velocity}}}")

    def build_command(self, **kwargs):
        command, params = self.value
        _tmp =params.format(**kwargs)
        tmp = eval(_tmp)
        return command, tmp

class ZoomError(Exception):
    pass

class Zoom:

    @staticmethod
    def _is_a_zoom_expanding(expand):
        return MobileCommands.ZOOM_AND_EXPAND if expand else MobileCommands.ZOOM_AND_REDUCE

    @staticmethod
    def _zooming(driver, command, id, percentage, velocity):
        try:
            driver.execute_script(
                *command.build_command(id=id, percentage=percentage, velocity=velocity)
            )
        except Exception as e:
            raise ZoomError("Unable to make zoom on selected element")

    @classmethod
    def make_zoom(cls, driver, locator, percentage=0.5, velocity=1.0, expand=True):
        """

        Run appium --use-plugins=gestures

        """
        element = driver.find_element(*locator)
        command = cls._is_a_zoom_expanding(expand=expand)
        cls._zooming(driver=driver,command=command, id=element.id, percentage=percentage, velocity=velocity)

    @classmethod
    def stepping_zoom(cls, driver, locator, stepping, percentage, velocity, expand=True):

        element = driver.find_element(*locator)
        command = cls._is_a_zoom_expanding(expand=expand)
        actual_percentage = 0
        while actual_percentage < percentage:
            actual_percentage += stepping
            cls._zooming(driver=driver,command=command, id=element.id, percentage=actual_percentage, velocity=velocity)
            time.sleep(0.2)