from list.list import List


class _Node:

    def __init__(self, value=None, next_node=None):
        self.__value = value
        self.__next_node = next_node

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_next(self, node):
        self.__next_node = node

    def get_next(self):
        return self.__next_node


# noinspection DuplicatedCode
class LinkedList(List):

    def __init__(self):
        self.__head = None
        self.__size: int = 0

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return self.__size == 0

    def append(self, elem) -> bool:
        if self.__size == 0:
            self.__head = _Node(elem)
        else:
            current: _Node = self.__head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(_Node(elem))
        self.__size += 1
        return True

    def insert_at(self, elem, at: int) -> bool:
        pass

    def add_all(self, other: 'List'):
        for i in range(other.size()):
            self.append(other.at(i))

    def at(self, at: int):
        assert 0 <= at < self.size()
        current: _Node = self.__head
        pos: int = 0
        while pos < at:
            current = current.get_next()
            pos = pos + 1
        return current.get_value()

    def remove_front(self):
        pass

    def remove_last(self):
        pass

    def remove_at(self, at: int):
        pass

    def __str__(self) -> str:
        rep: str = "["
        current: _Node = self.__head
        while current is not None:
            rep += str(current.get_value())
            if current.get_next() is not None:
                rep += ", "
            current = current.get_next()
        rep += "]"
        return rep
