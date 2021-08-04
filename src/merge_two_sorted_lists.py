from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        elif l1.val > l2.val:
            return ListNode(l2.val, next=self.mergeTwoLists(l1, l2.next))
        else:
            return ListNode(l1.val, next=self.mergeTwoLists(l1.next, l2))
