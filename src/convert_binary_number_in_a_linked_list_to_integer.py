from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        current_node: ListNode | None = head

        while current_node:
            answer = (answer << 1) + current_node.val
            current_node = current_node.next

        return answer
