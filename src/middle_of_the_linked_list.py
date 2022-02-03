from typing import Optional

OptNode = Optional["ListNode"]


class ListNode:
    def __init__(self, val: int = 0, next: OptNode = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: OptNode) -> OptNode:
        length = self.get_list_length(head)
        middle_index = length // 2
        return self.get_node_by_index(head, middle_index)

    def get_list_length(self, head: OptNode) -> int:
        if head is None:
            return 0
        return 1 + self.get_list_length(head.next)

    def get_node_by_index(self, head: OptNode, index: int) -> OptNode:
        assert index >= 0

        if head is None or index == 0:
            return head
        return self.get_node_by_index(head.next, index - 1)
