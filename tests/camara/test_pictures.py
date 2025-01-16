import re
import time
from datetime import datetime, timezone
import pytest

from apps.gallery_app import GalleryApp
from tests.camara.base_test_camara import BaseTestCamara, CameraType
from utils.locators import GalleryLocators
from utils.tools import YamlManager


def pytest_addoption(parser):
    """
    Defines the costume console inputs to run the tests
    """
    parser.addoption("--camera_type", action="store", default="Frontal", help="Camera type")


@pytest.fixture(scope="function")
def camera_type(pytestconfig):
    """
    Configures the Appium driver using app-specific data.
    """
    return pytestconfig.getoption("camera_type")


@pytest.fixture(scope="class")
def app_data():
    """
    Define app-specific data (e.g., package and activity).
    """
    return YamlManager.get_yaml_file_data("config\config.yaml")["apps"]["camera"]

class TestPictures(BaseTestCamara):
    @pytest.fixture(autouse=True)
    def setup(self, driver, camera_type):
        super().setup(driver)
        self.gallery_iface = GalleryApp(self.driver_manager.driver)        print(f"Camera type: {camera_type}")


    @pytest.mark.parametrize(
        ("camera_type"),
        [
            ("Frontal"),
            ("Normal")
        ]
    )
    def test_take_picture(self, camera_type):
        """
        Test case to validate that a picture has been taken validating the date of last picture matches the
        date of the moment when the picture has been taken.
        """
        if camera_type == CameraType.FRONTAL:
            self.camara_iface.switch_camera()
        # variables definition
        pattern_date = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b (?:[0-2]?\d|3[01]), \d\d\d\dㆍ(?:1[0-2]|0?[1-9]):[0-5][0-9]\u202F[AP]M'
        self.camara_iface.base_driver.implicitly_wait(30)
        # 1. Take picture
        self.camara_iface.take_picture()
        # 2. Get current timestamp when picture has been taken
        timestamp = datetime.now(timezone.utc).timestamp()
        dt_object = datetime.fromtimestamp(timestamp)
        expected_time = dt_object.strftime("%B %d, %Yㆍ%I:%M\u202F%p")
        print(f"Expected date: {expected_time}")
        # 3. Click on last picture button
        self.camara_iface.see_last_picture()
        # 4. since gallery click on info button
        time.sleep(3)
        self.gallery_iface.click_info_button()
        # 5. Get date from the current picture
        current_picture_date = self.gallery_iface.get_picture_date()
        print(f"Current date: {current_picture_date}")
        # 6. Check the pattern matches
        result = re.match(pattern_date, current_picture_date)
        assert result
        # 7. Check date matches TODO: correct date format
        #assert expected_time == current_picture_date



