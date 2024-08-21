from typing import Optional

from expressions.expression import Expression
from expressions.binary_expression import BinaryExpression, BinaryOp
from expressions.constant import Constant
from expressions.negation import Not
from expressions.variable import Variable


class ExpressionBuilder:
    """
    Builds a boolean expression, must call `build` to obtain the built expression
    """

    def __init__(self):
        self.__expression: Optional[Expression] = None

    def expression(self: 'ExpressionBuilder', expr: Expression) -> 'ExpressionBuilder':
        """
        Starts a new expression builder from a specific boolean expression
        :param expr: the boolean expression
        :return: a new expression builder with `expr` as the current expression
        """
        assert expr is not None
        assert self.__expression is None
        self.__expression = expr
        return self

    def constant(self: 'ExpressionBuilder', value: bool) -> 'ExpressionBuilder':
        """
        Starts a new expression builder from a constant value, i.e.: `True` or `False`
        :param value: the boolean constant
        :return: a new expression builder with a constant from `value` as the current expression
        """
        assert value is not None
        assert self.__expression is None
        self.__expression = Constant(value)
        return self

    def variable(self: 'ExpressionBuilder', var: str) -> 'ExpressionBuilder':
        """
        Starts a new expression builder from a variable name, i.e.: `"p"` or `"my_variable"`
        :param var: the variable's name
        :return: a new expression builder with a variable from `var` as the current expression
        """
        assert var is not None
        assert self.__expression is None
        self.__expression = Variable(var)
        return self

    def negate(self: 'ExpressionBuilder') -> 'ExpressionBuilder':
        """
        Negates the current expression
        :return: a new expression builder with the current expression being negated
        """
        assert self.__expression is not None
        self.__expression = Not(self.__expression)
        return self

    def disjunction(self: 'ExpressionBuilder', expr_right: Expression) -> 'ExpressionBuilder':
        """
        Creates a disjunction with another expression
        :param expr_right: the expression with which to create a new disjunction
        :return: a new expression builder with a disjunction of the current expression and `expr_right`
        """
        assert expr_right is not None
        assert self.__expression is not None
        self.__expression = BinaryExpression(self.__expression, expr_right, BinaryOp.OR)
        return self

    def conjunction(self: 'ExpressionBuilder', expr_right: Expression) -> 'ExpressionBuilder':
        """
        Creates a conjunction with another expression
        :param expr_right: the expression with which to create a new conjunction
        :return: a new expression builder with a conjunction of the current expression and `expr_right`
        """
        assert expr_right is not None
        assert self.__expression is not None
        self.__expression = BinaryExpression(self.__expression, expr_right, BinaryOp.AND)
        return self

    def build(self: 'ExpressionBuilder') -> Expression:
        """
        :return: the current built expression
        """
        assert self.__expression is not None
        return self.__expression
