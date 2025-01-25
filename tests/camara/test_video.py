"""
Test video test file
"""
import time
import pytest
from tests.camara.base_test_camara import BaseTestCamera, CameraType
from utils.tools import YamlManager


@pytest.fixture(scope="class")
def app_data():
    """
    Define app-specific data (e.g., package and activity).
    """
    return YamlManager.get_yaml_file_data("config\config.yaml")["apps"]["camera"]


@pytest.mark.Camera
class TestRecordVideo(BaseTestCamera):
    """
    Record vide test class
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        super().setup(driver)
        self.camera_iface.change_to_video()

    @pytest.mark.Sanity
    @pytest.mark.parametrize(
        ("camera_type", "record_time", "pauses"),
        [
            ("Frontal", 5.5, 1),
            ("Normal", 8.1, 1)
        ]
    )
    def test_record_video(self, camera_type, record_time, pauses):
        """
        Test case to record video, making some pauses, and re enable, either frontal or normal camera

        Args:
            camera_type(CameraType): Type of camera, Frontal or Normal
            record_time(float): Time in seconds to record
            pauses(int/float): Time in seconds to perform pauses between recordings
        """
        if camera_type == CameraType.FRONTAL:
            self.camera_iface.switch_camera()

        # start to record
        self.camera_iface.take_picture()
        current_time = time.time()
        while  time.time() < current_time + record_time:
            time.sleep(pauses)
            self.camera_iface.pause_recording()
        self.camera_iface.stop_recording()
