from typing import Dict, Optional

from expressions.expression import Expression


class Constant(Expression):
    """
    A constant boolean expression, either `True` or `False`
    """

    def __init__(self: 'Constant', value: bool):
        self.__value = value

    def variables(self: 'Constant') -> [str]:
        return []

    def interpretations(self: 'Constant') -> [Dict[str, bool]]:
        return []

    def evaluate(self: 'Constant', interpretation: Dict[str, bool]) -> bool:
        return self.__value

    def __str__(self):
        return str(self.__value)