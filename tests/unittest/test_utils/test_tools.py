"""
Test file to validate tools.py file
"""
import unittest
from utils.tools import MathUtils, MathUtilsError
from parameterized import parameterized

class InvalidStrObject:
    """Invalid object to make an invalid str conversion"""
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return int(self._value)

class TestMathUtils(unittest.TestCase):
    """
    Unit test class to validate MathUtils class.
    """

    @parameterized.expand(
        [
            ("Addition", 1236, ["+" for _ in range(3)], 12),
            ("Subtraction", 1236, ["-" for _ in range(3)], -10),
            ("Multiplication", 1236, ["*" for _ in range(3)], 36),
            ("Division", 1236, ["/" for _ in range(3)], 0.028),
        ]
    )
    def test_valid_value(self, name, numbers, operations, expected_result):
        """
        Validate valid values for arithmetic_operation_seq_number method
    
        Args:
            name(str): Type of operation, just informative
            numbers(int): Sequence of numbers to perform operation
            operations(list): list of operations to perform over numbers
            expected_result(float/int): Expected result
        """
        print(f"Testing: {name}")
        result = round(MathUtils.arithmetic_operation_seq_number(numbers, operations), 3)
        self.assertEqual(result, expected_result)

    @parameterized.expand(
        [
            ("123fvds"),
            ("{}2aq"),
            ("HOLA"),
            ("onetrheseven"),
            (None)
        ]
    )
    def test_invalid_pattern(self, invalid_object):
        """
        Test to validate invalid parameters to enter to arithmetic_operation_seq_number

        Args:
            invalid_object(Any): Invalid type of input
        """
        operations = ["+" for _ in range(3)]
        with self.assertRaises(expected_exception=MathUtilsError) as e:
            MathUtils.arithmetic_operation_seq_number(invalid_object,operations)
        actual_exception = e.expected
        self.assertEqual(actual_exception, MathUtilsError)

    def test_type_error(self):
        """
        Validate arithmetic_operation_seq_number raises the expected exception
        when an invalid object, which cannot be converted to str is introduce
        """
        invalid_obj = InvalidStrObject("3")
        operations = ["+" for _ in range(3)]
        with self.assertRaises(expected_exception=TypeError) as e:
            MathUtils.arithmetic_operation_seq_number(invalid_obj, operations)
        actual_exception = e.expected
        self.assertEqual(actual_exception, TypeError)


if __name__ == "__main__":
    unittest.main()