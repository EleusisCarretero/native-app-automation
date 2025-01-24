"""
Test picture file
"""
import re
import time
import pytest
from datetime import datetime, timezone
from apps.gallery_app import GalleryApp
from tests.camara.base_test_camara import BaseTestCamara, CameraType
from utils.tools import YamlManager


@pytest.fixture(scope="class")
def app_data():
    """
    Define app-specific data (e.g., package and activity).
    """
    return YamlManager.get_yaml_file_data("config\config.yaml")["apps"]["camera"]

class TestPictures(BaseTestCamara):
    """
    Test picture class

    Attributes:
        gallery_iface(GalleryApp): instance to interface gallery app
    """
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        super().setup(driver)
        self.gallery_iface = GalleryApp(self.driver_manager.driver)

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
        TODO: Figureo out how to pass 'cameratype' as a console input just for this test, or any camera test

        Args:
            camera_type (CameraType) : Camera type, Frontal or Normal
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
        time.sleep(2)
        self.camara_iface.see_last_picture()
        # 4. since gallery click on info button
        self.gallery_iface.click_info_button()
        # 5. Get date from the current picture
        current_picture_date = self.gallery_iface.get_picture_date()
        print(f"Current date: {current_picture_date}")
        # 6. Check the pattern matches
        result = re.match(pattern_date, current_picture_date)
        assert result
        # 7. Check date matches TODO: correct date format
        #TODO: assert expected_time == current_picture_date

    @pytest.mark.parametrize(
        ("camera_type"),
        [
            ("Frontal"),
            ("Normal")
        ]
    )
    def test_make_zoom(self, camera_type):
        """
        Test class to check zoom in the different cameras. TODO: missing assertions

        Args:
            camera_type(CameraType): Type of camera
        """
        if camera_type == CameraType.FRONTAL:
            self.camara_iface.switch_camera()
        self.camara_iface.zoom_camera(percentage=0.75, velocity=1.0, expand=True)
        time.sleep(1)
        self.camara_iface.zoom_camera(percentage=0.60, velocity=1.0, expand=False)
        time.sleep(1)
        self.camara_iface.stepping_zoom_camera(stepping=0.05,percentage=0.15, velocity=1.0, expand=True)
        time.sleep(3)
        self.camara_iface.take_picture()
        time.sleep(2)
