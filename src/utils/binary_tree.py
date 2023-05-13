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

    def __repr__(self) -> str:
        return f"Node({self.val})"


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    if not root:
        return []

    real_node_count = 1
    result: list[int | None] = []
    to_visit: typing.Deque[TreeNode | None] = deque()
    to_visit.append(root)

    while to_visit:
        node = to_visit.popleft()
        result.append(node.val if node else None)
        if node:
            real_node_count -= 1

            if not real_node_count and not (node.left or node.right):
                break

            to_visit.append(node.left)
            to_visit.append(node.right)

            if node.left:
                real_node_count += 1
            if node.right:
                real_node_count += 1

    return result


def list_to_tree(lst: list[int]) -> TreeNode | None:
    if not lst:
        return None

    items = iter(lst)
    to_visit: typing.Deque[TreeNode | None] = deque()
    head = TreeNode(next(items))
    to_visit.append(head)

    while to_visit:
        node = to_visit.popleft()
        assert node

        try:
            left_val = next(items)
            left = None if left_val is None else TreeNode(left_val)
            node.left = left
            if left:
                to_visit.append(left)

            right_val = next(items)
            right = None if right_val is None else TreeNode(right_val)
            node.right = right
            if right:
                to_visit.append(right)
        except StopIteration:
            break

    return head


def find_node(tree: TreeNode | None, x: int) -> TreeNode | None:
    if not tree:
        return None
    if tree.val == x:
        return tree
    return find_node(tree.left, x) or find_node(tree.right, x)


__all__ = ["TreeNode", "tree_to_list", "list_to_tree", "find_node"]
