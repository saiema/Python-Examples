from comparable.comparable import Comparable
from typing import Union, List


class BinarySearchTree:
    """
    A Binary Search Tree, construction of this tress are dependent on the static functions:
    `BinarySearchTree.binary_search_tree()`
    and
    `BinarySearchTree.nil()`
    """

    @staticmethod
    def binary_search_tree(value: Comparable,
                           left: 'BinarySearchTree',
                           right: 'BinarySearchTree') -> 'BinarySearchTree':
        """
        Constructs a new tree with a root value and two subtrees (left and right)
        :param value: The value of the root
        :param left: The left subtree
        :param right: The right subtree
        :return: a new Binary Search Tree with `value` as the root, `left` and `right` subtrees
        """
        assert value is not None
        assert left is not None
        assert right is not None
        return BinarySearchTree(value, left, right)

    @staticmethod
    def nil():
        """
        Returns an empty Binary Search Tree
        :return: an empty Binary Search Tree
        """
        return BinarySearchTree(None, None, None)

    def __init__(self: 'BinarySearchTree',
                 value: Union[Comparable, None],
                 left: Union['BinarySearchTree', None],
                 right: Union['BinarySearchTree', None]):
        self.__root = value
        self.__left = left
        self.__right = right

    def rep_ok(self) -> bool:
        """
        Validates the invariants of a Binary Search Tree
        :return: `True` if this is a Binary Search Tree
        """
        if self.__root is None:
            return True
        if self.is_leaf():
            return True
        if not self.__is_acyclic():
            return False
        if not self.__binary_search_tree_order():
            return False
        return True

    def __binary_search_tree_order(self: 'BinarySearchTree') -> bool:
        """
        Determines that the order of the nodes are correctly ordered:
        All nodes in the left subtree are less than the root; all nodes in the
        right subtree are greater than the root; and this property holds for all nodes in the tree
        :return: `True` iff the nodes are ordered correctly with respect to a Binary Search Tree
        """
        if self.__root is None or self.is_leaf():
            return True
        else:
            for v in self.__left.inorder():
                if self.__root.compare_to(v) <= 0:
                    return False
            for v in self.__right.inorder():
                if self.__root.compare_to(v) >= 0:
                    return False
            return self.__left.__binary_search_tree_order() and self.__right.__binary_search_tree_order()

    def __is_acyclic(self: 'BinarySearchTree') -> bool:
        """
        Determines if a Binary Search Tree is acyclic (does not contain cycles)
        :return: `True` iff the Binary Search Tree does not contain any cycle
        """
        return self.__is_acyclic_recursive([])

    def __is_acyclic_recursive(self: 'BinarySearchTree', visited_values: List[Comparable]) -> bool:
        if self.__root is None:
            return True
        elif self.__root in visited_values:
            return False
        visited_values.append(self.__root)
        if not self.__left.__is_acyclic_recursive(visited_values):
            return False
        if not self.__right.__is_acyclic_recursive(visited_values):
            return False
        return True

    def is_empty(self: 'BinarySearchTree') -> bool:
        """
        Checks whether this tree is empty
        :return: `True` iff this tree is empty
        """
        if self.__root is None:
            return True

    def size(self: 'BinarySearchTree') -> int:
        """
        Returns the size (number of nodes) of this tree
        :return: the size (number of nodes) of this tree
        """
        if self.__root is None:
            return 0
        else:
            return 1 + self.__left.size() + self.__right.size()

    def is_leaf(self: 'BinarySearchTree') -> bool:
        """
        Checks whether this tree only has a root and no children
        :return: `True` iff this tree has a root and does not have left and right children
        """
        return self.__root is not None and self.__left.is_empty() and self.__right.is_empty()

    def add_value(self: 'BinarySearchTree', value: Comparable) -> 'BinarySearchTree':
        """
        Returns a new Binary Search Tree with the given value added
        :param value: the value to add
        :return: a new Binary Search Tree with `value` added or this tree if `value` is already
        in the tree
        """
        if self.__root is None:
            return BinarySearchTree.binary_search_tree(value,
                                                       BinarySearchTree.nil(),
                                                       BinarySearchTree.nil()
                                                       )
        elif self.__root.compare_to(value) == 0:
            return self
        elif self.__root.compare_to(value) < 0:
            return BinarySearchTree.binary_search_tree(self.__root,
                                                       self.__left,
                                                       self.__right.add_value(value)
                                                       )
        elif self.__root.compare_to(value) > 0:
            return BinarySearchTree.binary_search_tree(self.__root,
                                                       self.__left.add_value(value),
                                                       self.__right
                                                       )

    def remove_value(self: 'BinarySearchTree', value: Comparable) -> 'BinarySearchTree':
        """
        Removes a value to this tree, if the value is present
        :param value: the value to remove
        :return: a new Binary Search Tree with `value` removed
        """
        if self.__root is None:
            return self
        elif self.is_leaf() and self.__root.compare_to(value) == 0:
            return BinarySearchTree.nil()
        elif self.__root.compare_to(value) < 0:
            return BinarySearchTree.binary_search_tree(self.__root,
                                                       self.__left,
                                                       self.__right.remove_value(value))
        elif self.__root.compare_to(value) > 0:
            return BinarySearchTree.binary_search_tree(self.__root,
                                                       self.__left.remove_value(value),
                                                       self.__right)
        else:  # the root is the value but we have children
            if self.__left.is_empty():
                return self.__right
            elif self.__right.is_empty():
                return self.__left
            else:  # we have a left and a right child
                minimum: Comparable = self.__right.get_minimum()
                new_right: 'BinarySearchTree' = self.__right.remove_value(minimum)
                return BinarySearchTree.binary_search_tree(minimum, self.__left, new_right)

    def get_value(self: 'BinarySearchTree', value: Comparable) -> Union[Comparable, None]:
        """
        Return the value of this tree that matches a certain value,
        the value that matches the value to search might have more information than the
        value provided.
        :param value: the value to search
        :return: `None`, or a value matching `value`
        """
        if self.__root is None:
            return None
        elif self.__root.compare_to(value) == 0:
            return self.__root
        elif self.__root.compare_to(value) < 0:
            return self.__right.get_value(value)
        else:
            return self.__left.get_value(value)

    def get_minimum(self: 'BinarySearchTree') -> Union[Comparable, None]:
        """
        Returns the minimum value of a binary search tree, or None if the tree is empty
        :return: the minimum value in this binary search tree, or `None` if the tree is empty
        """
        if self.__root is None:
            return None
        elif self.is_leaf():
            return self.__root
        elif self.__left is not None:
            return self.__left.get_minimum()
        else:
            return self.__root

    def get_maximum(self: 'BinarySearchTree') -> Union[Comparable, None]:
        """
        Returns the maximum value of a binary search tree, or None if the tree is empty
        :return: the maximum value in this binary search tree, or `None` if the tree is empty
        """
        if self.__root is None:
            return None
        elif self.is_leaf():
            return self.__root
        elif self.__right is not None:
            return self.__right.get_maximum()
        else:
            return self.__root

    def contains_value(self: 'BinarySearchTree', value: Comparable) -> bool:
        """
        Checks is a value exists in this tree
        :param value: the value to search
        :return: `True` iff `value` exists in the tree
        """
        if self.__root is None:
            return False
        elif self.__root.compare_to(value) == 0:
            return True
        elif self.__root.compare_to(value) < 0:
            return self.__right.contains_value(value)
        else:
            return self.__left.contains_value(value)

    def inorder(self: 'BinarySearchTree') -> [Comparable]:
        """
        Returns a list with all the values in the inorder traversal
        :return: a list with all tree nodes following the inorder traversal
        """
        if self.__root is None:
            return []
        else:
            return self.__left.inorder() + [self.__root] + self.__right.inorder()

    def json(self: 'BinarySearchTree') -> str:
        """
        Returns a JSON representation of this tree
        :return: a JSON representation of this tree
        """
        if self.__root is None:
            return "{root: Nil, left: Nil, right: Nil}"
        elif self.is_leaf():
            return "{root: " + str(self.__root) + ", left: Nil, right: Nil}"
        else:
            return "{root: " + str(self.__root) + \
                ", left: " + self.__left.json() + \
                ", right: " + self.__right.json() + "}"

    def __str__(self) -> str:
        return str([str(x) for x in self.inorder()])
