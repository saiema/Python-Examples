from list.list import List
from list.linked_list import LinkedList
from list.cheating_list import CheatingList

if __name__ == "__main__":
    list1: List = LinkedList()
    list2: List = CheatingList()

    list1.append(1)
    list1.append(2)
    list1.append(3)

    print("list1 is {}\n".format(str(list1)))

    list2.append(4)
    list2.append(5)
    list2.append(6)

    print("list2 is {}\n".format(str(list2)))

    list1.add_all(list2)

    print("list1 is {}\n".format(str(list1)))
