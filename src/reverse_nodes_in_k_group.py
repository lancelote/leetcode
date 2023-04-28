from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def get_length(self, node: ListNode | None) -> int:
        if node is None:
            return 0

        length = 0

        while node is not None:
            length += 1
            node = node.next

        return length

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        length = self.get_length(head)
        times = length // k

        dummy = ListNode(-1, next=head)
        section_prev = dummy

        prev = dummy
        curr = dummy.next

        for _ in range(times):
            for _ in range(k):
                assert curr

                tmp = curr
                curr = curr.next
                tmp.next = prev
                prev = tmp

            assert section_prev.next

            tmp = section_prev
            section_prev = section_prev.next
            tmp.next = prev
            section_prev.next = curr
            prev = section_prev

        return dummy.next
