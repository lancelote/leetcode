import typing
from collections import deque

from src.utils.binary_tree import TreeNode


def tree_to_list(root: TreeNode | None) -> list[int]:
    result: list[int] = []
    to_visit: typing.Deque[TreeNode | None] = deque()
    to_visit.append(root)

    while to_visit:
        node = to_visit.popleft()
        if node:
            result.append(node.val)
            to_visit.append(node.left)
            to_visit.append(node.right)

    return result


def insert(root: TreeNode | None, value: int | None) -> TreeNode | None:
    if value is None:
        pass
    elif root is None:
        return TreeNode(value)
    elif value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def list_to_tree(values: list[int | None]) -> TreeNode | None:
    root = None

    for value in values:
        root = insert(root, value)

    return root


__all__ = ["TreeNode", "tree_to_list", "list_to_tree"]
