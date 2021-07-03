from __future__ import annotations

from typing import List
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.val})"


def insert(root: Optional[TreeNode], value: int) -> TreeNode:
    if not root:
        return TreeNode(value)
    elif value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def create_tree(values: List[int]) -> Optional[TreeNode]:
    root = None

    for value in values:
        root = insert(root, value)

    return root


class Solution:
    def rangeSumBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> int:
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )
