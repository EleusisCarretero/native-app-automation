"""
Pytest conftest file
"""
import pytest
from utils.driver import AppiumDriverManager
from appium.webdriver.appium_service import AppiumService


def pytest_addoption(parser):
    """
    Defines the costume console inputs to run the tests

    device_name: Device name
    """
    parser.addoption("--device_name", action="store", default="Galaxy A33", help="Device name")


@pytest.fixture(scope="function")
def driver(pytestconfig, app_data):
    """
    Configures the Appium driver using app-specific data.
    """
    device_name = pytestconfig.getoption("device_name")

    driver_manager = AppiumDriverManager(
        device_name=device_name,
        **app_data,
    )
    driver_manager.start_driver()
    yield driver_manager
    driver_manager.stop_driver()


@pytest.fixture(scope="class")
def appium_server(appium_settings):
    """
    Initialize the Appium server

    Args:
        appium_settings(list): List of Appium server options
    """
    appium_service = AppiumService()
    appium_service.start(args=appium_settings)
    if appium_service.is_running:
        print("Appium server is running!")
    yield
    appium_service.stop()

    if not appium_service.is_running:
        print("Appium server has stopped.")
