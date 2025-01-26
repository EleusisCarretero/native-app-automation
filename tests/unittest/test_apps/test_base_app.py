"""
Unit-test for Base_app.py file
"""
import unittest
from unittest.mock import Mock, patch
from xml.sax.xmlreader import Locator

from parameterized import parameterized
from appium.webdriver.common.appiumby import AppiumBy
from apps.base_app import BaseApp, BaseAppError


class TestBaseApp(unittest.TestCase):
    """
    Unit-test class to validate BaseApp
    """
    @parameterized.expand(
        [
            ("Invalid_locator"),
            (189),
            (2.9),
            ((AppiumBy.ID, "com.sec.android.app.dummyapp:id/dummy_id", "Extra"))
        ]
    )
    def test_click_app_button_in_valid_locator(self, *locator):
        _mock_driver = Mock()
        base_app = BaseApp(_mock_driver)
        with self.assertRaises(expected_exception=BaseAppError) as e:
            base_app.click_app_button(locator=Locator)
        actual_exception = e.expected
        self.assertEqual(actual_exception, BaseAppError)

    @patch("apps.base_app.webdriver.Remote.find_element")
    @patch("apps.base_app.webdriver.Remote")  #
    def test_click_button_methods(self, remo_driver, mock_find_element):
        # Define variables
        _element = 1
        _base_app = BaseApp(remo_driver)
        _locator = (AppiumBy.ID, "com.sec.android.app.dummyapp:id/dummy_id")

        # Define mock returns
        mock_bttn_obj = Mock()
        mock_find_element.return_value = mock_bttn_obj

        # Call method under test
        _base_app.click_app_button(locator=_locator)

        # Validate assertions
        mock_find_element.assert_called_with(*_locator)
        mock_bttn_obj.click.assert_called_once()

if __name__ == "__main__":
    unittest.main()
