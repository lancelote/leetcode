from __future__ import annotations


class Node:
    def __init__(
        self, x: int, next: Node | None = None, random: Node | None = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        old_nodes: dict[Node, int] = {}
        new_nodes: dict[int, Node] = {}

        # construct map of old nodes
        i = 0
        current: Node | None = head

        while current:
            old_nodes[current] = i

            i += 1
            current = current.next

        # construct copy without random
        dummy = Node(-1)
        new_current = dummy

        i = 0
        current = head

        while current:
            new_node = Node(x=current.val)
            new_current.next = new_node
            new_current = new_node
            new_nodes[i] = new_node

            i += 1
            current = current.next

        # set random in copy
        i = 0
        current = head
        new_head: Node | None = dummy.next

        while current:
            assert new_head

            if current.random:
                new_head.random = new_nodes[old_nodes[current.random]]

            i += 1
            current = current.next
            new_head = new_head.next

        return dummy.next
