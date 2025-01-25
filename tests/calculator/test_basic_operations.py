"""
Test basic operations file
"""
import pytest
from tests.calculator.base_test_calculator import BaseTestCalculator
from utils.tools import YamlManager, MathUtils


@pytest.fixture(scope="class")
def app_data():
    """
    Define app-specific data (e.g., package and activity).
    """
    return YamlManager.get_yaml_file_data("config\config.yaml")["apps"]["calculator"]


def sequenced_operation(type_of_op):
    """
    Function to assign the corresponding parametrized params

    Args:
        type_of_op(str): desired operation type

    Return:
        Tuple: corresponding parameters.
    """

    return {
        "simple_add":  [
                (897),
                (87531),
                (753149)
        ],
        "simple_sub": [
                (897),
                (87531),
                (753149)
        ],
        "simple_mul": [
                (897),
                (87531),
                (753149)
        ],
        "simple_div":  [
                (897),
                (87531),
                (753149)
        ],
        "simple_ops": [ 
            (897, ['+', '*']),
            (87531, ['/','*', '+', '-']),
            (753149, ['+', '+', '/', '/', '*'])
        ]
    }.get(type_of_op, None)


@pytest.mark.Calculator
class TestBasicOperations(BaseTestCalculator):
    """
    Test basic calculator operations class
    """
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        super().setup(driver)

    @pytest.mark.Smoke
    @pytest.mark.parametrize(
            ("number"), sequenced_operation("simple_add")
    )
    def test_simple_addition(self, number):
        """
        Test case to evaluate a simple sum of unit numbers.

        Args:
            number(int): Sequence of unit numbers
        """
        len_operation = len(str(number)) - 1
        operations=["+" for _ in range(len_operation)]
        result = self.cal_iface.single_seq_operation(num=number, operations=operations)
        assert int(result) == MathUtils.arithmetic_operation_seq_number(number, operations)

    @pytest.mark.Sanity
    @pytest.mark.parametrize(
            ("number"), sequenced_operation("simple_sub")
    )
    def test_simple_subtraction(self, number):
        """
        Test case to evaluate a simple subtraction of unit numbers.

        Args:
            number(int): Sequence of unit numbers
        """
        len_operation = len(str(number)) - 1
        operations=["-" for _ in range(len_operation)]
        result = self.cal_iface.single_seq_operation(num=number, operations=operations)
        assert int(result) == MathUtils.arithmetic_operation_seq_number(number, operations)

    @pytest.mark.Sanity
    @pytest.mark.parametrize(
            ("number"), sequenced_operation("simple_mul")
    )
    def test_simple_mul(self, number):
        """
        Test case to evaluate a simple multiplication of unit numbers.

        Args:
            number(int): Sequence of unit numbers
        """
        len_operation = len(str(number)) - 1
        operations=["*" for _ in range(len_operation)]
        result = self.cal_iface.single_seq_operation(num=number, operations=operations)
        assert float(result) == MathUtils.arithmetic_operation_seq_number(number, operations)

    @pytest.mark.Sanity
    @pytest.mark.parametrize(
            ("number"), sequenced_operation("simple_div")
    )
    def test_simple_div(self, number):
        """
        Test case to evaluate a simple division of unit numbers.

        Args:
            number(int): Sequence of unit numbers
        """
        len_operation = len(str(number)) - 1
        operations=["/" for _ in range(len_operation)]
        result = self.cal_iface.single_seq_operation(num=number, operations=operations)
        assert round(float(result), 9) == round(MathUtils.arithmetic_operation_seq_number(number, operations), 9)

    @pytest.mark.Soak
    @pytest.mark.parametrize(
            ("number", "operations"), sequenced_operation("simple_ops")
    )
    def test_simple_operations(self, number, operations):
        """
        Test case to evaluate a mix of simple operations over a sequence of unit numbers
        Args:
            number(int): Sequence of unit numbers
            operations(list): list of arithmetic operations to do
        """
        result = self.cal_iface.single_seq_operation(num=number, operations=operations)
        print(f"Result: {result}")
        assert round(float(result), 9) == round(MathUtils.arithmetic_operation_seq_number(number, operations), 9)

    @pytest.mark.Smoke
    @pytest.mark.parametrize(
        ("value"),
        [9, 1, 6]
    )
    def test_unit_percentage(self, value):
        """
        Test case to evaluate percentage figure is working by convertin a
        number in percentage.

        Args:
            value(int): value to convert in percentage
        """
        self.cal_iface.tap_num(value)
        self.cal_iface.percentage()
        self.cal_iface.equals_to()
        actual_percentage = self.cal_iface.result()
        assert str(value / 100) == actual_percentage

    @pytest.mark.Smoke
    def test_bigger_that_units_numbers(self):
        """
        Test case to check the basic arithmetic operation over a number bigger than a unit.
        """
        list_numbers = [123,98,345,736]
        operations = ["+" for _ in range(len(list_numbers) - 1)]
        res = self.cal_iface.large_seq_operation(list_numbers,operations)
        print(res)
        assert res
