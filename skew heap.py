class SkewNode(object):
        def __init__(self, value, left = None, right = None):
                self._value = value
                self._left = left
                self._right = right

        def left(self):
                return self._left

        def right(self):
                return self._right

        def swap(self):
                self._right, self._left = self._left, self._right

        def value(self):
                return self._value

        def copy(self):
                return SkewNode(self._value, left = self._left.copy() if self._left is not None else None, right = self._right.copy() if self._right is not None else None)

class SkewHeap(object):
        def __init__(self, root = None):
                self._root = root

        def root(self):
                return self._root

        def insert(self, value):
                new = SkewHeap(SkewNode(value))
                self.merge(new)

        def empty(self):
                return self._root is None

        def top(self):
                if self._root is None:
                        raise ValueError
                return self._root.value()

        def pop(self):
                result = self._root.value()
                merger = SkewHeap(self._root._right)
                self._root = self._root._left
                self.merge(merger)
                return result

        def extend(self, iterable):
                for item in iterable:
                        self.insert(item)

        def merge(self, other):
                if other.empty():
                        return
                if self.empty():
                        self._root = other._root.copy()
                        return
                if self.top() > other.top():
                        self._root, other = other._root.copy(), SkewHeap(self._root)
                self._root.swap()
                merger = SkewTree(self._left).merge(other)
                self._root._left = merger.root()


if __name__ == "__main__":
        h = SkewHeap()
        assert h.empty()
        h.insert(2)
        h.insert(32)
        h.insert(42)
        h.insert(1)
        assert not h.empty()
        assert h.top() == 1
        p = h.pop()
        assert p == 1
        assert h.pop() == 2
        assert h.pop() == 32
        assert h.pop() == 42
        assert h.empty()
