"""
Contains common functions, constants, classes that can be util but not
necessary is part of a feature.
"""
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


def arithmetic_operation_seq_number(sequence_num, arithmetic_op):
    res = 0
    for i, num in enumerate(str(sequence_num)):
        if i == 0:
            res = float(num)
        else:
            res = eval(f"{res}{arithmetic_op[i-1]}{num}")
    return res


