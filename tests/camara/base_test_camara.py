"""
BaseTestCamera file and relates
"""
from enum import Enum
from apps.camera_app import CameraApp
from apps.gallery_app import GalleryApp
from tests.base_test import BaseTest


class CameraType(str, Enum):
    """Type camera"""
    FRONTAL = "Frontal"
    NORMAL = "Normal"

class BaseTestCamera(BaseTest):
    """
    Paren of all test camera classes

    Attributes:
        camera_iface(CameraApp): instance interface for app
        gallery_iface(GalleryApp): instance to interface gallery app
    """
    def setup(self, driver):
        super().setup(driver)
        self.gallery_iface = GalleryApp(self.driver_manager.driver)
        self.camera_iface = CameraApp(self.driver_manager.driver)
