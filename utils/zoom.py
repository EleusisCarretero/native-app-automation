"""
Zoom class file.
To be able to execute the script commands is needed to start appium server using the next flag:
    Run appium --use-plugins=gestures
"""
import time


class ScriptCommands:
    """
    General class for script commands available to be executed by the 'driver' (WebDriver)
    Attributes:
        name (str): command name with the format type: command
        kwargs (dict): input parameters for the command
    """
    def __init__(self, name, **kwargs):
        self.name = name
        self.params_commands = {k: v for k, v in kwargs.items()}

    def command(self, **kwargs):
        """
        Builds the format of the inputs parameters for the command.

        Args:
            kwargs (dict): values to fill the original needed parameters

        Returns:
            tuple: command, parameters filled
        """
        return self.name, {k:v.format(**kwargs) for k, v in self.params_commands.items()}


class MobileCommands(ScriptCommands):
    """
    Specif 'mobile' commands
    Attributes:
        MOBILE (str): mobile command
    """
    MOBILE = "mobile"
    def __init__(self, name, **kwargs):
       super().__init__(name=f"{self.MOBILE}: {name}", **kwargs)


class ZoomError(Exception):
    pass

class Zoom:
    """
    Class Zoom to control the expansion and reduction in a screen
    """
    ZOOM_AND_EXPAND = MobileCommands(f"pinchOpenGesture", elementId='{id}', percent='{percentage}',
                                     velocity='{velocity}')
    ZOOM_AND_REDUCE = MobileCommands(f"pinchCloseGesture", elementId='{id}', percent='{percentage}',
                                     velocity='{velocity}')

    @classmethod
    def _is_a_zoom_expanding(cls, expand):
        """
        Determines if the type of the zoom is positive or negative

        Args:
            expand (Boolean): Flag to choose type of zoom

        Returns:
            MobileCommands: Type of zoom, positive or negative
        """
        return cls.ZOOM_AND_EXPAND if expand else cls.ZOOM_AND_REDUCE

    @staticmethod
    def _zooming(driver, command, id, percentage, velocity):
        try:
            driver.execute_script(
                *command.command(id=id, percentage=percentage, velocity=velocity)
            )
        except Exception as e:
            raise ZoomError("Unable to make zoom on selected element")

    @classmethod
    def make_zoom(cls, driver, locator, percentage=0.5, velocity=1.0, expand=True):
        """
        Method to perform a positive or negative Zoom

        Args:
            driver (Webdriver): driver instance of the current session
            locator (Tuple): locator of the element to zooming
            percentage (float): Percentage of zoom
            velocity (float): velocity to perform the zoom
            expand (boolean): flag to indicate the sense of the zooming
        """
        element = driver.find_element(*locator)
        command = cls._is_a_zoom_expanding(expand=expand)
        cls._zooming(driver=driver,command=command, id=element.id, percentage=percentage, velocity=velocity)

    @classmethod
    def stepping_zoom(cls, driver, locator, stepping, percentage, velocity, expand=True, wait_time=0.2):
        """
        Method to perform a positive or negative Zoom by doing small increases, stepping

        Args:
            driver (Webdriver): driver instance of the current session
            locator (Tuple): locator of the element to zooming
            stepping (float): value to stepping
            percentage (float): Percentage of zoom
            velocity (float): velocity to perform the zoom
            expand (boolean): flag to indicate the sense of the zooming
            wait_time (float): time in seconds to wait before to the next zoom.
        """
        element = driver.find_element(*locator)
        command = cls._is_a_zoom_expanding(expand=expand)
        actual_percentage = 0
        while actual_percentage < percentage:
            actual_percentage += stepping
            cls._zooming(driver=driver,command=command, id=element.id, percentage=actual_percentage, velocity=velocity)
            time.sleep(wait_time)
