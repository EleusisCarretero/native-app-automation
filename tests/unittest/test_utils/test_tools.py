import unittest
from utils.tools import MathUtils, MathUtilsError
from parameterized import parameterized

class InvalidStrObject:
    def __str__(self):
        raise ValueError("Cannot convert to string")

class TestMathUtils(unittest.TestCase):

    @parameterized.expand(
        [
            ("Addition", 1236, ["+" for _ in range(3)], 12),
            ("Subtraction", 1236, ["-" for _ in range(3)], -10),
            ("Multiplication", 1236, ["*" for _ in range(3)], 36),
            ("Division", 1236, ["/" for _ in range(3)], 0.028),
        ]
    )
    def test_valid_value(self, name, numbers, operations, expected_result):
        print(f"Testing: {name}")
        result = round(MathUtils.arithmetic_operation_seq_number(numbers, operations), 3)
        self.assertEqual(result, expected_result)

    @parameterized.expand(
        [
            ("123fvds"),
            ("{}2aq"),
            ("HOLA"),
            ("onetrheseven"),
        ]
    )
    def test_invalid_pattern(self, invalid_object):
        operations = ["+" for _ in range(3)]
        with self.assertRaises(expected_exception=MathUtilsError) as e:
            MathUtils.arithmetic_operation_seq_number(invalid_object,operations)
        actual_exception = e.expected
        self.assertEqual(actual_exception, MathUtilsError)




if __name__ == "__main__":
    unittest.main()