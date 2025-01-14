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


class TestBasicOperations(BaseTestCalculator):

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        super().setup(driver)

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
