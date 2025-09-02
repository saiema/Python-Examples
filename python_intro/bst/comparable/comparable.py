from abc import ABC, abstractmethod


class Comparable(ABC):

    @abstractmethod
    def compare_to(self: 'Comparable', other: 'Comparable') -> int:
        """
        Compares this value, against another
        :param other: the other value to compare with
        :return: a negative value if this is less than `other`; zero if this is equal to `other`; positive otherwise
        """
        pass

    @abstractmethod
    def value(self):
        """
        Returns the associated value of this Comparable instance
        :return: the associated value of this Comparable instance
        """
        pass
