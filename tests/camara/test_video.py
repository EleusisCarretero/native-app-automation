import time

import pytest
from tests.camara.base_test_camara import BaseTestCamara, CameraType
from apps.gallery_app import GalleryApp
from utils.tools import YamlManager


@pytest.fixture(scope="class")
def app_data():
    """
    Define app-specific data (e.g., package and activity).
    """
    return YamlManager.get_yaml_file_data("config\config.yaml")["apps"]["camera"]


class TestRecordVideo(BaseTestCamara):

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        super().setup(driver)
        self.gallery_iface = GalleryApp(self.driver_manager.driver)
        self.camara_iface.change_to_video()

    @pytest.mark.parametrize(
        ("camera_type", "record_time", "pauses"),
        [
            ("Frontal", 5.5, 1),
            ("Normal", 8.1, 1)
        ]
    )
    def test_record_video(self, camera_type, record_time, pauses):
        if camera_type == CameraType.FRONTAL:
            self.camara_iface.switch_camera()

        # start to record
        self.camara_iface.take_picture()
        current_time = time.time()
        while  time.time() < current_time + record_time:
            time.sleep(pauses)
            self.camara_iface.pause_recording()
        self.camara_iface.stop_recording()
