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


def sum_seq_number(sequence_num):
    """
    Return a sequence number sum. 

    Ex:
        123 -> 1+2+3 -> 6
    
    Returns:
        int: sum of input
    """
    return sum([int(n) for n in str(sequence_num)])

def subs_seq_number(sequence_num):
    """
    Returns a sequence number subtraction.

    Ex:
        123 -> 1-2-3 -> -4
    
    Returns:
        int: subtraction of input
    """
    _subs = 0
    for i, n in enumerate(str(sequence_num)):
        if i == 0:
            _subs = int(n)
        else:
            _subs -= int(n)
    return _subs

def mul_sep_number(sequence_num):
    _mul = 1
    for n in str(sequence_num):
        _mul *= float(n)
    return _mul

def div_seq_number(sequence_num):
    _div = 0
    for i, n in enumerate(str(sequence_num)):
        if i == 0:
            _div = float(n)
        else:
            _div /= float(n)
    return _div
