"""
BaseTestCamera file and relates
"""
from enum import Enum
from apps.camara_app import CamaraApp
from tests.base_test import BaseTest


class CameraType(str, Enum):
    """Type camera"""
    FRONTAL = "Frontal"
    NORMAL = "Normal"

class BaseTestCamera(BaseTest):
    """
    Paren of all test camera classes

    Attributes:
        camera_iface(CamaraApp): instance interface for app
    """
    def setup(self, driver):
        super().setup(driver)
        self.camera_iface = CamaraApp(self.driver_manager.driver)
