from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        bits: list[str] = []

        while head:
            bits.append(str(head.val))
            head = head.next

        return int("".join(bits), 2)
