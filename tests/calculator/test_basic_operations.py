import os
import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy

from apps.calculator_app import CalculatorApp
from utils.tools import YamlManager, div_seq_number, mul_sep_number, subs_seq_number, sum_seq_number


@pytest.fixture(scope="class")
def app_data():
    """
    Define app-specific data (e.g., package and activity).
    """
    return YamlManager.get_yaml_file_data("config\config.yaml")["apps"]["calculator"]


class TestBasicOperations:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver_manager = driver
        self.cal_iface = CalculatorApp(self.driver_manager.driver)
    
    
    
    @pytest.mark.parametrize(
            ("number"),
            [
                (897),
                (87531),
                (753149)
            ]
    )
    def test_simple_addition(self, number):
        """
        Test case to evaluate a simple sum of unit numbers.

        Args:
            number(int): Sequence of unit numbers
        """
        len_operation = len(str(number)) - 1
        result = self.cal_iface.single_seq_operation(num=number, operations=["+" for _ in range(len_operation)])
        assert int(result) == sum_seq_number(number)

    @pytest.mark.parametrize(
            ("number"),
            [
                (897),
                (87531),
                (753149)
            ]
    )
    def test_simple_subtraction(self, number):
        """
        Test case to evaluate a simple subtraction of unit numbers.

        Args:
            number(int): Sequence of unit numbers
        """
        len_operation = len(str(number)) - 1
        result = self.cal_iface.single_seq_operation(num=number, operations=["-" for _ in range(len_operation)])
        assert int(result) == subs_seq_number(number)

    @pytest.mark.parametrize(
            ("number"),
            [
                (897),
                (87531),
                (753149)
            ]
    )
    def test_simple_mul(self, number):
        len_operation = len(str(number)) - 1
        result = self.cal_iface.single_seq_operation(num=number, operations=["*" for _ in range(len_operation)])
        assert int(result) == mul_sep_number(number)
    
    @pytest.mark.parametrize(
            ("number"),
            [
                (897),
                (87531),
                (753149)
            ]
    )
    def test_simple_div(self, number):
        len_operation = len(str(number)) - 1
        result = self.cal_iface.single_seq_operation(num=number, operations=["/" for _ in range(len_operation)])
        assert int(result) == div_seq_number(number)
