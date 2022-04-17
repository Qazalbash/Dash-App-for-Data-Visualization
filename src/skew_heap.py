from skew_node import *


class SkewHeap:
    """
    A SkewHeap is a heap data structure which uses an unbalanced binary tree to
    store items. Although no attempt is made to balance the tree, it can be
    shown to have amortized O(log n) time complexity for all operations under
    the assumption that the items inserted are in random order.
    """

    def __init__(self, items=tuple()):
        """
        SkewHeap() -> new, empty, skew heap.
        SkewHeap(iterable) -> new skew heap initialized from the iterable.
        """
        self.root: Node = None
        for item in items:
            self.push(item)

    def push(self, value: Any):
        """Add an item to this heap."""
        node = Node(value, None, None)
        self.root = merge(self.root, node)

    def pop(self):
        """Remove the least item in this heap and return it."""
        if self.root is None:
            raise ValueError("Cannot pop empty SkewHeap")
        else:
            value = self.root.value
            self.root = merge(self.root.left, self.root.right)
            return value

    def peek(self):
        """Return the least item in this heap without modifying this heap."""
        if self.root is None:
            raise ValueError("Cannot peek into empty SkewHeap")
        else:
            return self.root.value

    def union(self, other: "SkewHeap") -> "SkewHeap":
        """Return a new heap which contains all the items of this and another heap combined."""
        ret = SkewHeap()
        ret.root = merge(self.root, other.root)
        return ret

    def __add__(self, other: "SkewHeap") -> "SkewHeap":
        """The plus operator returns the union of two SkewHeaps."""
        return self.union(other)

    def __len__(self) -> int:
        """Return the number of items in this heap."""
        return count(self.root)

    def __bool__(self) -> bool:
        """Return true iff the heap is non-empty."""
        return self.root is not None

    def depth(self) -> int:
        """Return the depth of the tree used to represent this skew heap."""
        return depth(self.root)
