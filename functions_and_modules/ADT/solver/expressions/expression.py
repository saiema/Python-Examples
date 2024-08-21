from abc import ABC, abstractmethod
from typing import Dict, Optional


class Expression(ABC):
    """
    Base class for all boolean expressions
    """

    @staticmethod
    def _recursive_interpretations(interpretations: [[(str, bool)]], variables: [str]) -> [[(str, bool)]]:
        """
        Private method to calculate all possible interpretations for a given set of variables
        Callers of this function should create a dictionary for every interpretation returned
        :param interpretations: an initial list of interpretations
        :param variables: the variables for which interpretations will be generated
        :return: a list of all possible interpretations (lists of tuples with the format `(var, bool_value)`
        """
        if len(variables) == 0:
            return interpretations
        previous_interpretations: [[(str, bool)]] = Expression._recursive_interpretations(
            interpretations, variables[1:]
        )
        return [[(variables[0], True)] + inter for inter in previous_interpretations]\
            + [[(variables[0], False)] + inter for inter in previous_interpretations]

    @abstractmethod
    def variables(self: 'Expression') -> [str]:
        """
        Returns a list of all variables involved in this expression
        :return: the list of all variables involved in this expression
        """
        pass

    @abstractmethod
    def interpretations(self: 'Expression') -> [Dict[str, bool]]:
        """
        Returns a list of all possible interpretations for this expression
        :return: a list of all possible interpretations for this expression
        """
        pass

    @abstractmethod
    def evaluate(self: 'Expression', interpretation: Dict[str, bool]) -> bool:
        """
        Evaluates an expression on a particular interpretation of the expression's variables
        :param interpretation: a particular interpretation of the expression's variables
        :return: `True` iff the expression is true under `interpretation`
        """
        pass

    @abstractmethod
    def __str__(self):
        """
        Returns the string representation of this expression
        :return: the string representation of this expression
        """
        pass
