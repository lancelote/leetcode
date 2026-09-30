class Node:
    def __init__(
        self, x: int, next: Node | None = None, random: Node | None = None
    ) -> None:
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        if head is None:
            return None

        old_to_new: dict[Node, Node] = {}

        dummy = Node(0)
        new_current = dummy
        old_current = head

        while old_current is not None:
            new_node = Node(old_current.val, random=old_current.random)
            old_to_new[old_current] = new_node

            new_current.next = new_node

            old_current = old_current.next
            new_current = new_current.next

        new_current = dummy
        while new_current is not None:
            if new_current.random is not None:
                new_current.random = old_to_new[new_current.random]

            new_current = new_current.next

        return dummy.next
