from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(
        self, head: ListNode | None = None, prev_val: int | None = None
    ) -> ListNode | None:
        if head is None:
            return None
        first_node = prev_val is None
        if first_node or prev_val != head.val:
            return ListNode(
                val=head.val,
                next=self.deleteDuplicates(head.next, prev_val=head.val),
            )
        if prev_val == head.val:
            return self.deleteDuplicates(head.next, prev_val=head.val)
        return None
