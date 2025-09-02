from my_collections.binary_search_tree import BinarySearchTree
from comparable.comparable_int import ComparableInt
from sys import argv

if __name__ == '__main__':
    tree_a = BinarySearchTree.nil()
    values = [int(arg) for arg in argv[1:]]
    for value in values:
        tree_a = tree_a.add_value(ComparableInt(value))
        print(str(tree_a))
        print(tree_a.json())
        print(tree_a.rep_ok())
