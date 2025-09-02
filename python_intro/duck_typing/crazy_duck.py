from typing import Any, List


class CrazyDuck:

    def __init__(self: 'CrazyDuck', name: str = "Howard"):
        self.__name: str = name
        self.__cuacks: List[Any] = []

    def add_cuack(self: 'CrazyDuck', cuack: Any) -> None:
        self.__cuacks.append(cuack)

    def __str__(self: 'CrazyDuck') -> str:
        return "I'm {} the Duck, and my cuacks are {}".format(self.__name, str(self.__cuacks))
    
    def __getitem__(self: 'CrazyDuck', item: Any) -> Any:
        if item == "name":
            return self.__name
        elif item == "cuacks":
            return self.__cuacks
        elif item == "my first cuack":
            if self.__cuacks is None or len(self.__cuacks) == 0:
                return "I never had a cuack!"
            else:
                return self.__cuacks[0]
        elif isinstance(item, int):
            if item == 0:
                return self.__name
            elif item > 0:
                return self.__cuacks[item - 1]
            else:
                return self.__cuacks[item]
            
    def __eq__(self: 'CrazyDuck', value: Any):
        if value is None:
            return False
        if not isinstance(value, CrazyDuck):
            return False
        else:
            if self.__name != value.__name:
                return False
            if self.__cuacks is None:
                return value.__cuacks is None
            if len(self.__cuacks) != len(value.__cuacks):
                return False
            for (my_cuack, others_cuack) in zip(self.__cuacks, value.__cuacks):
                if my_cuack != others_cuack:
                    return False
        return True
