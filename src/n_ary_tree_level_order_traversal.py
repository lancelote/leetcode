from __future__ import annotations


class Node:
    def __init__(
        self, val: int | None = None, children: list[Node] | None = None
    ):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node | None) -> list[list[int]]:
        if root is None:
            return []

        level = [root]
        result: list[list[int]] = []

        while level:
            result.append([node.val for node in level if node.val is not None])

            new_level: list[Node] = []
            for node in level:
                if node.children is not None:
                    for child in node.children:
                        new_level.append(child)
            level = new_level

        return result
