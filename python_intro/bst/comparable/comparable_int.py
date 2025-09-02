from comparable.comparable import Comparable


class ComparableInt(Comparable):

    def __init__(self: 'ComparableInt', value: int):
        self.__value = value

    def compare_to(self: 'ComparableInt', other: 'ComparableInt') -> int:
        return self.__value - other.__value

    def value(self) -> int:
        return self.__value

    def __str__(self) -> str:
        return str(self.__value)
