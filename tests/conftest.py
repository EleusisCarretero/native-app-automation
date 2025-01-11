import pytest
from utils.driver import AppiumDriverManager


def pytest_addoption(parser):
    """
    Defines the costume console inputs to run the tests
    """
    parser.addoption("--device_name", action="store", default="Galaxy A33", help="Device name")

@pytest.fixture(scope="class")
def driver(pytestconfig, app_data):
    """
    Configures the Appium driver using app-specific data.
    """
    device_name = pytestconfig.getoption("device_name")

    app_package = app_data["app_package"]
    app_activity = app_data["app_activity"]

    driver_manager = AppiumDriverManager(
        app_package=app_package,
        app_activity=app_activity,
        device_name=device_name
    )
    driver_manager.start_driver()
    yield driver_manager
    driver_manager.stop_driver()

