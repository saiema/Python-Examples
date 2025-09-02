from abc import ABC, abstractmethod


class List(ABC):
    """
    An abstract list, a linearly ordered collection of elements.
    """

    @abstractmethod
    def size(self) -> int:
        """
        Returns the size of the current list
        :return: how many elements does this list contains
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Checks if this list is empty or not
        :return: `True` iff this list is empty (equivalent to call size() == 0)
        """
        pass

    @abstractmethod
    def append(self, elem) -> bool:
        """
        Appends an element to the end of the list
        :param elem: the element to append
        :return: `True` iff the element was successfully appended
        """
        pass

    @abstractmethod
    def insert_at(self, elem, at: int) -> bool:
        """
        Inserts an element at a specific position, moving all original elements
        from that position and forward, one position to the right.
        :param elem: the element to insert
        :param at: the position, must be greater or equal to `0`, if it's greater or equal than
        the size of the list, the function call will behave as calling :func:`append`.
        :return: `True` iff the element was successfully appended
        """
        pass

    @abstractmethod
    def add_all(self, other: 'List'):
        """
        Appends all elements of another list into this one
        :param other: the other list to append
        """
        pass

    @abstractmethod
    def at(self, at: int):
        """
        Returns the element at a specific position
        :param at: the position to the element to return, must be a valid position
        :return: the element at the specified position
        """
        pass

    @abstractmethod
    def remove_front(self):
        """
        Removes the element at the front of the list
        Requires a non-empty list
        :return: The element at the front of the list
        """
        pass

    @abstractmethod
    def remove_last(self):
        """
        Removes the element at the end of the list
        Requires a non-empty list
        :return: The element at the end of the list
        """
        pass

    @abstractmethod
    def remove_at(self, at: int):
        """
        Removes the element at a specific position
        :param at: the position of the element to remove, it must be a valid position.
        :return: The element removed
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns a string representation of a list.
        The expected representation starts with a `[` symbol;
        has all elements' representation separated by a comma and a space;
        finally ends with a `]` symbol.
        :return: The string representation of a list
        """
        pass
