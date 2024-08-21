from enum import Enum
from typing import Dict

from expressions.expression import Expression


class BinaryOp(Enum):
    """
    Enumeration of possible binary operators
    """
    AND = "AND"
    OR = "OR"


class BinaryExpression(Expression):
    """
    A binary expression, this expression can be evaluated to `True` or `False` depending on the evaluation of the
    underlying left and right expressions.
    """

    def __init__(self: 'BinaryExpression', left: Expression, right: Expression, op: BinaryOp):
        assert left is not None
        assert right is not None
        assert op is not None
        self.__type = op
        self.__left = left
        self.__right = right

    def variables(self: 'BinaryExpression') -> [str]:
        vars_set: [str] = []
        for var in self.__left.variables():
            if var not in vars_set:
                vars_set.append(var)
        for var in self.__right.variables():
            if var not in vars_set:
                vars_set.append(var)
        return vars_set

    def interpretations(self: 'BinaryExpression') -> [Dict[str, bool]]:
        interpretations_lists: [[(str, bool)]] = Expression._recursive_interpretations([[]], self.variables())
        return [dict(inter) for inter in interpretations_lists]

    def evaluate(self: 'BinaryExpression', interpretation: Dict[str, bool]) -> bool:
        if self.__type == BinaryOp.AND:
            return self.__left.evaluate(interpretation) and self.__right.evaluate(interpretation)
        else:
            return self.__left.evaluate(interpretation) or self.__right.evaluate(interpretation)

    def __str__(self):
        return str("({}) {} ({})".format(str(self.__left), str(self.__type.name), str(self.__right)))
