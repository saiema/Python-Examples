from typing import Dict, Optional

from expressions.expression import Expression


class Variable(Expression):
    """
    A variable expression, represents a boolean variable, with a specific name, this variable can be evaluated
    to `True` or `False` depending on the interpretation, e.g.: `p` is `True` only for an
    interpretation including `[("p", True)]`
    """

    def __init__(self: 'Variable', var: str):
        self.__var = var

    def variables(self: 'Variable') -> [str]:
        return [self.__var]

    def interpretations(self: 'Variable') -> [Dict[str, bool]]:
        return [dict[(self.__var, True)], dict[(self.__var, False)]]

    def evaluate(self: 'Variable', interpretation: Dict[str, bool]) -> bool:
        assert self.__var in interpretation.keys()
        return interpretation[self.__var]

    def __str__(self):
        return str(self.__var)
