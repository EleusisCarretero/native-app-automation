"""
Click gesture class and relates
"""
from utils.zoom import MobileCommands


class ClickError(Exception):
    """Click exception"""


class Click:
    """
    Click class to manage tap gestures
    """
    TAP = MobileCommands("clickGesture", x = '{x}', y = '{y}')
    LONG_CLICK = MobileCommands("longClickGesture", x = '{x_coo}', y = '{y_coo}', duration = '{duration}')
    DRAG_AND_DROP = MobileCommands("dragGesture", startX = '{startX}', startY = '{startY}', endX = '{endX}', endY = '{endY}')

    @classmethod
    def _execution(cls, driver, command, **kwargs):
        """
        Execute script

        Args:
            driver (Webdriver): driver instance of the current session
            command (MobileCommands): Gesture command with its arguments
            kwargs(): Value for the command arguments

        Raise:
            ClickError: Unable to perform the script execution
        """
        try:
            driver.execute_script(
                *cls._convert_coo_param_to_int(command=command, **kwargs)
            )
        except Exception as e:
            raise ClickError("Unable to perform gesture") from e
    
    @staticmethod
    def _convert_coo_param_to_int(command, **kwargs):
        cmd , params = command.command(**kwargs)
        return cmd, {k:int(v) for k,v in params.items()}

    @classmethod
    def tap_on_coordinate(cls, driver, x, y):
        """
        Method to perform a tap on a specific coordinate

        Args:
            driver (Webdriver): driver instance of the current session
            x(int): x coordinate
            y(int): y coordinate
        """
        cls._execution(driver=driver,command=cls.TAP, x=x, y=y)
