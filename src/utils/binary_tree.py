from __future__ import annotations

import typing
from collections import deque


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.val})"


def insert(root: TreeNode | None, value: int | None) -> TreeNode | None:
    if not value:
        pass
    elif not root:
        return TreeNode(value)
    elif value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def list_to_tree(values: list[int]) -> TreeNode | None:
    root = None

    for value in values:
        root = insert(root, value)

    return root


def tree_to_list(root: TreeNode | None) -> list[int]:
    result = []
    to_visit: typing.Deque[TreeNode | None] = deque()
    to_visit.append(root)

    while to_visit:
        node = to_visit.popleft()
        if node:
            result.append(node.val)
            to_visit.append(node.left)
            to_visit.append(node.right)

    return result
