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
        with open(file_path, "r") as file:
            content = yaml.safe_load(file)
        return content

class MathUtilsError(Exception):
    pass

class MathUtils:

    @staticmethod
    def arithmetic_operation_seq_number(sequence_num, arithmetic_op):
        pattern_num = r'^-?\d+(\.\d+)?$'
        try:
            str_sequence_num = str(sequence_num)
        except TypeError:
            raise MathUtilsError(f"Unable to convert {sequence_num} to str")
        if not re.match(pattern_num, str_sequence_num):
            raise MathUtilsError("'arithmetic_op' should be a string of number between 0-9")
        res = 0
        for i, num in enumerate(str_sequence_num):
            if i == 0:
                res = float(num)
            else:
                res = eval(f"{res}{arithmetic_op[i-1]}{num}")
        return res
    
    @staticmethod
    def increment_current_time(current_time, increment:float):
        _hr, _min = str(increment).split(".")
        new_hr = current_time.hour + int(_hr)
        new_min = current_time.minute + int(_min)
        current_time.replace(hour=new_hr, minute=new_min)
        return current_time
