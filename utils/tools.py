"""
Contains common functions, constants, classes that can be util but not
necessary is part of a feature.
"""
import re
import os
import yaml


class YamlManager:
    """
    Class which handle with yaml file stuff, as well load info, write, etc
    """

    @staticmethod
    def get_yaml_file_data(relative_path):
        """Return a dictionary with the content from the given 'relative_path' parameter"""
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_dir, relative_path)
        content = {}
        with open(file_path, "r", encoding="utf-8") as file:
            content = yaml.safe_load(file)
        return content

class MathUtilsError(Exception):
    """MathUtils Error"""

class MathUtils:
    """
    Math utils class
    """
    @staticmethod
    def arithmetic_operation_seq_number(sequence_num, arithmetic_op):
        """
        Perform a sequence of simple arithmetic operations

        Args:
            sequence_num(int): Sequence of numbers
            arithmetic_op(list): List of str with the arithmetic operation
        
        Returns:
            int/float: Result of the operation
        """
        pattern_num = r'^-?\d+(\.\d+)?$'
        try:
            str_sequence_num = str(sequence_num)
        except TypeError as e:
            raise MathUtilsError(f"Unable to convert {sequence_num} to str") from e
        if not re.match(pattern_num, str_sequence_num):
            raise MathUtilsError("'arithmetic_op' should be a string of number between 0-9")
        res = 0
        for i, num in enumerate(str_sequence_num):
            if i == 0:
                res = float(num)
            else:
                res = eval(f"{res}{arithmetic_op[i-1]}{num}")  # noqa: W0123
        return res
    
    @staticmethod
    def increment_current_time(current_time, increment:float):
        """
        Increment the given time in hours, or/and minutes
        Args:
            current_time: Current time to increment
            increment(float): Value in hr.min to make conversion, ex 1.3 -> 1h with 30 mins
        """
        _hr, _min = str(increment).split(".")
        new_hr = current_time.hour + int(_hr)
        new_min = current_time.minute + int(_min)
        dt_modified = current_time.replace(hour=new_hr, minute=new_min)
        return dt_modified
