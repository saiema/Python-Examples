from typing import Dict, Optional

from expressions.expression import Expression


class Not(Expression):
    """
    A negated expression, this expression can be evaluated to `True` or `False` depending on the evaluation of the
    negated expression, e.g.: `not p` is `True` for an interpretation including `[("p", False)]`
    """

    def __init__(self: 'Not', expr: Expression):
        assert expr is not None
        self.__expr = expr

    def variables(self: 'Not') -> [str]:
        return self.__expr.variables()

    def interpretations(self: 'Not') -> [Dict[str, bool]]:
        interpretations_lists: [[(str, bool)]] = Expression._recursive_interpretations([[]], self.variables())
        return [dict(inter) for inter in interpretations_lists]

    def evaluate(self: 'Not', interpretation: Dict[str, bool]) -> bool:
        return not self.__expr.evaluate(interpretation)

    def __str__(self):
        return str("not ({})".format(str(self.__expr)))
