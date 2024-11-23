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
    def process_child(
        self, child: Node | None, prev: Node | None, leftmost: Node | None
    ) -> tuple[Node | None, Node | None]:
        if child:
            if prev:
                prev.next = child
            else:
                leftmost = child
            prev = child
        return prev, leftmost

    def connect(self, root: Node | None) -> Node | None:
        if not root:
            return None

        leftmost: Node | None = root

        while leftmost:
            prev = None
            curr: Node | None = leftmost
            leftmost = None

            while curr:
                prev, leftmost = self.process_child(curr.left, prev, leftmost)
                prev, leftmost = self.process_child(curr.right, prev, leftmost)

                curr = curr.next

        return root
