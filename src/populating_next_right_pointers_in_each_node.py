from __future__ import annotations


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Node | None = None,
        right: Node | None = None,
        next: Node | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node | None) -> Node | None:
        if root is None:
            return None

        leftmost = root

        while leftmost.left is not None:
            head = leftmost

            while head:
                assert head.left is not None

                head.left.next = head.right

                if head.next:
                    assert head.right is not None

                    head.right.next = head.next.left

                head = head.next

            leftmost = leftmost.left

        return root
