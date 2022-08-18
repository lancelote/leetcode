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


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    if not root:
        return []

    result: list[int | None] = []
    to_visit: typing.Deque[TreeNode | None] = deque()
    to_visit.append(root)

    while to_visit:
        node = to_visit.popleft()
        result.append(node.val if node else None)
        if node and (node.left or node.right):
            to_visit.append(node.left)
            to_visit.append(node.right)

    return result


def list_to_tree(lst: list[int]) -> TreeNode | None:
    if not lst:
        return None

    items = iter(lst)
    to_visit: typing.Deque[TreeNode | None] = deque()
    head = TreeNode(next(items))
    to_visit.append(head)

    while to_visit:
        node = to_visit.pop()

        if not node:
            continue

        try:
            left_val = next(items)
            left = TreeNode(left_val) if left_val else None
            node.left = left
            to_visit.append(left)

            right_val = next(items)
            right = TreeNode(right_val) if right_val else None
            node.right = right
            to_visit.append(right)
        except StopIteration:
            break

    return head


__all__ = ["TreeNode", "tree_to_list", "list_to_tree"]
