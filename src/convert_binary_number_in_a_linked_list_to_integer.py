from __future__ import annotations

from src.utils.linked_list import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        current_node: ListNode | None = head

        while current_node:
            answer = (answer << 1) + current_node.val
            current_node = current_node.next

        return answer
