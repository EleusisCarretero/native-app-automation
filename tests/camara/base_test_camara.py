import pytest
from enum import Enum
from apps.camara_app import CamaraApp
from tests.base_test import BaseTest


class CameraType(str, Enum):
    FRONTAL = "Frontal"
    NORMAL = "Normal"

class BaseTestCamara(BaseTest):
    def setup(self, driver):
        super().setup(driver)
        self.camara_iface = CamaraApp(self.driver_manager.driver)