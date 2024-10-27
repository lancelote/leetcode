from __future__ import annotations


class Node:
    def __init__(
        self, x: int, next: Node | None = None, random: Node | None = None
    ) -> None:
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        old_to_new: dict[Node, Node] = {}

        dummy = Node(-1)

        old = head
        new = dummy

        while old:
            node = Node(old.val, random=old.random)
            new.next = node
            new = node

            old_to_new[old] = node
            old = old.next

        current = dummy.next

        while current:
            if current.random:
                current.random = old_to_new[current.random]
            current = current.next

        return dummy.next
