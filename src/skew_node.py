from typing import NamedTuple, Any, Optional


class Node(NamedTuple):
    """A single Node in a binary tree."""

    def __init__(self, value, left, right) -> None:

        self.value: Any = value
        self.left: Node = left
        self.right: Node = right


def count(node: Optional[Node]) -> int:
    """Count the total number of nodes in a tree rooted at this node."""
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)


def depth(node: Optional[Node]) -> int:
    """Determine the depth of the tree under this node."""
    if node is None:
        return 0
    return 1 + max(depth(node.left), depth(node.right))


def merge(p: Optional[Node], q: Optional[Node]) -> Node:
    """
    Implements the critical "merge" operation which is
    used by all operations on a SkewHeap. The merge operation
    does not mutate either tree but returns a new tree which
    contains the least item at the root and is in heap order.
    The resulting tree is not necessarily balanced.
    """
    if p is None:
        return q
    if q is None:
        return p

    if q.value < p.value:
        p, q = q, p

    return Node(p.value, merge(p.right, q), p.left)
