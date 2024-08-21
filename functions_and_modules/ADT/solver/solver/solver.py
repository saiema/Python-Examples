from typing import Dict, Optional, List

from expressions.expression import Expression


def solve(expression: Expression) -> bool:
    """
    Solves the expression to determine if it's true or not
    :param expression: the expression to solve
    :return: `True` iff the expression can be made `True` by some interpretation.
    """
    pass


def is_sat(expression: Expression) -> Optional[Dict[str, bool]]:
    """
    Returns an interpretation i such that the expression can be satisfied, i.e.: `evaluate(i)` is `True`
    :param expression: the expression to evaluate
    :return: an interpretation `i` if `i` satisfies this expression, `None` otherwise
    """
    pass


def satisfies(expression: Expression) -> Optional[List[Dict[str, bool]]]:
    """
    Returns all interpretations i such that the expression is satisfied, i.e.: `evaluate(i)` is `True`
    :param expression: the expression to evaluate
    :return: all interpretations `i` such that `i` satisfies this expression, `None` otherwise
    """
    pass


def not_satisfies(expression: Expression) -> Optional[List[Dict[str, bool]]]:
    """
    Returns all interpretations i such that the expression is not satisfied, i.e.: `evaluate(i)` is `False`
    :param expression: the expression to evaluate
    :return: all interpretations `i` such that `i` does not satisfy this expression, `None` otherwise
    """
    pass


def is_tautology(expression: Expression) -> bool:
    """
    Checks if an expression is a tautology
    :param expression: the expression to evaluate
    :return: `True` iff `expression` is `True` under all possible interpretations
    """
    pass


def is_contradiction(expression: Expression) -> bool:
    """
    Checks if an expression is a contradiction
    :param expression: the expression to evaluate
    :return: `True` iff `expression` is `False` under all possible interpretations
    """
    pass
