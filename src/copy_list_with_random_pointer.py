from __future__ import annotations


class Node:
    def __init__(
        self, x: int, next: Node | None = None, random: Node | None = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self) -> str:
        return f"Node({self.val})"


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        new_dummy = Node(-1)
        old_dummy = Node(-1, next=head)

        old_to_new: dict[Node | None, Node | None] = {None: None}

        new_current = new_dummy
        old_current = old_dummy

        while old_current.next:
            old_current = old_current.next
            new_node = Node(old_current.val)
            new_current.next = new_node
            new_current = new_current.next

            old_to_new[old_current] = new_current

        new_current = new_dummy
        old_current = old_dummy

        while old_current.next and new_current.next:
            old_current = old_current.next
            new_current = new_current.next
            new_current.random = old_to_new[old_current.random]

        return new_dummy.next
