class Node:
    def __init__(self, value, parent=None):
        self._parent = parent
        self._left = None
        self._right = None
        self._value = value
        self._quantity = 1

    def __repr__(self):
        if self._left is None and self._right is None:
            return f'{self._value}'
        return f'{self._value} ({self._left}, {self._right})'

    def __eq__(self, other):
        return self._value == other

    def __gt__(self, other):
        return self._value > other

    def __lt__(self, other):
        return self._value < other

    def __le__(self, other):
        return self._value <= other

    def __ge__(self, other):
        return self._value >= other

    def insert(self, value):
        if value < self._value:
            if self._left is None:
                self._left = Node(value, self)
            else:
                self._left.insert(value)
        elif value > self._value:
            if self._right is None:
                self._right = Node(value, self)
            else:
                self._right.insert(value)
        else:
            self._quantity += 1

class Tree:
    def __init__(self, iterable=()):
        self._root = None
        for value in iterable:
            self.insert(value)

    def insert(self, value):
        if self._root is None:
            self._root = Node(value)
        else:
            self._root.insert(value)

    def __iter__(self):
        return self._traverse_in_order(self._root)

    def reverse(self):
        return self._traverse_in_reverse(self._root)

    def __contains__(self, value):
        return self._contains(self._root, value)

    def __repr__(self):
        return repr(self._root)

    def _traverse_in_order(self, node):
        if node is not None:
            yield from self._traverse_in_order(node._left)
            yield node._value
            yield from self._traverse_in_order(node._right)

    def _traverse_in_reverse(self, node):
        if node is not None:
            yield from self._traverse_in_reverse(node._right)
            yield node._value
            yield from self._traverse_in_reverse(node._left)

    def _contains(self, node, value):
        if node is None:
            return False
        if node._value == value:
            return True
        elif value < node._value:
            return self._contains(node._left, value)
        else:
            return self._contains(node._right, value)

def bubble_sort(data: list, reverse=False) -> list:
    nums = len(data)
    changes = True
    while changes:
        changes = False
        for spot in range(0, nums - 1):
            if (data[spot] > data[spot + 1] and not reverse) or (data[spot] < data[spot + 1] and reverse):
                data[spot], data[spot + 1] = data[spot + 1], data[spot]
                changes = True
    return data

def bisect_search(sorted_data: list, value) -> int:
    low, high = 0, len(sorted_data) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_data[mid] == value:
            return mid
        elif sorted_data[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def merge_sort(data: list, reverse=False) -> list:
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid], reverse)
    right = merge_sort(data[mid:], reverse)
    return _merge(left, right, reverse)

def _merge(left: list, right: list, reverse=False) -> list:
    result = []
    while left and right:
        if (left[0] <= right[0] and not reverse) or (left[0] > right[0] and reverse):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result
