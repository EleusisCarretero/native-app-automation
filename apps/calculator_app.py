from enum import Enum
from apps.base_app import BaseApp
from utils.locators import CalculatorLocators

class NumButton(int, Enum):
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


class CalculatorAppError(Exception):
    pass

class CalculatorApp(BaseApp):
    
    def tap_num(self, num:NumButton):
        if num not in NumButton:
            raise CalculatorAppError(f"{num} is not an allow number")
        self.click_app_button(CalculatorLocators.get_num_locator(num=num))

    def enter_big_number(self, num):
        try:
            mirror = 0
            while num > 0:
                num, res = divmod(num, 10)
                mirror = mirror * 10 + res
       

            while mirror > 0:
                mirror, res = divmod(mirror, 10)
                yield res
        finally:
            print("no more numbers")
