from list.list import List


class CheatingList(List):

    def __init__(self):
        self.__list = []

    def size(self) -> int:
        return len(self.__list)

    def is_empty(self) -> bool:
        return len(self.__list) == 0

    def append(self, elem) -> bool:
        self.__list.append(elem)
        return True

    def insert_at(self, elem, at: int) -> bool:
        self.__list.insert(at, elem)
        return True

    def add_all(self, other: 'List'):
        for i in range(other.size()):
            self.__list.append(other.at(i))

    def at(self, at: int):
        return self.__list[at]

    def remove_front(self):
        return self.__list.pop(0)

    def remove_last(self):
        return self.__list.pop(self.size())

    def remove_at(self, at: int):
        assert 0 <= at < self.size()
        return self.__list.pop(at)

    def __str__(self) -> str:
        return str(self.__list)
