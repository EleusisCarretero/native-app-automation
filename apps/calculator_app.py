"""
Calculator class file, as well as other related to it.
"""
from enum import Enum
import time
from apps.base_app import BaseApp
from utils.locators import CalculatorLocators

class NumButton(int, Enum):
    """
    Decimal numbers
    """
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    ZERO = 0

class Operations(str, Enum):
    """
    Simple arithmetic operations
    """
    PLUS = "+"
    MINUS = "-"
    MUL = "*"
    DIV = "/"
    EQUALS = "="


class CalculatorAppError(Exception):
    """
    Error class for CalculatorApp
    """
    pass

class CalculatorApp(BaseApp):
    """
    CalculatorApp Class manages the interation with Calculator native app. Controlling the number input, operations, etc
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.sequence = None
        self.MAP_OPE = {
            Operations.PLUS: self.addition,
            Operations.EQUALS: self.equals_to,
            Operations.MINUS: self.subtraction,
            Operations.MUL: self.multiplication,
            Operations.DIV: self.division
        }

    def tap_num(self, num:NumButton):
        """
        Method to tap on the button number.

        Args:
            num(NumButton): button number (0-9)
        """
        if num not in NumButton:
            raise CalculatorAppError(f"{num} is not an allow number")
        self.click_app_button(CalculatorLocators.get_num_locator(num=num))

    def equals_to(self):
        """
        Method to clicks on the 'equals' symbol.
        """
        self.click_app_button(CalculatorLocators.get_op_locator(op="Calculation"))

    def result(self):
        """
        Method to get the value frm result layout. included the '-' when it detects a 'Minus'.

        Returns:
            str: string number, or '-' string number
        """
        response = self.get_text(CalculatorLocators.get_result()).split()
        if 'Minus' in response:
            return "-" + response[1].replace(",","")
        return response[0].replace(",","")

    def addition(self):
        """
        Method to click on addition button.
        """
        self.click_app_button(CalculatorLocators.get_op_locator(op="Plus"))

    def subtraction(self):
        """
        Method to click on subtraction button.
        """
        self.click_app_button(CalculatorLocators.get_op_locator(op="Minus"))
    
    def multiplication(self):
        """
        Method to click on 'Multiplication' button.
        """
        self.click_app_button(CalculatorLocators.get_op_locator(op="Multiplication"))
    
    def division(self):
        """
        Method to click on 'Division' button.
        """
        self.click_app_button(CalculatorLocators.get_op_locator(op="Division"))

    def set_sequence_number(self, num):
        """
        Method to get the individual number of a 'sequenced' number bigger to 9.

        Ex. 123, it get the 1,2,3 individually

        Args:
            num: number bigger to 9
        Returns:
            int: Enter number from 0 to 9.
        """
        try:
            mirror = 0
            while num > 0:
                num, res = divmod(num, 10)
                mirror = mirror * 10 + res
       

            while mirror > 0:
                mirror, res = divmod(mirror, 10)
                self.sequence = mirror
                yield res
        finally:
            self.sequence = None
            print("no more numbers")
        
    def single_seq_operation(self, num, operations):
        """
        Method to perform simple operations with number no bigger to 9.

        Args:
            num(int): number bigger to 9.
            operations(list): list of simple arithmetic operation
        
        Returns:
            str: number from result gotten after operations.
        """
        for i, digit in enumerate(self.set_sequence_number(num)):
            self.tap_num(digit)
            if self.sequence > 0:
                self.MAP_OPE[operations[i]]()
            time.sleep(0.25)
        self.equals_to()
        return str(self.result())
