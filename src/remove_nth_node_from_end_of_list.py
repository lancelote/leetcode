from typing import Optional

OptNode = Optional["ListNode"]


class ListNode:
    def __init__(self, val: int = 0, next: OptNode = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: OptNode, n: int) -> OptNode:
        dummy = ListNode(next=head)
        left: OptNode = dummy
        right: OptNode = head

        for _ in range(n):
            if right:
                right = right.next

        while right:
            assert isinstance(left, ListNode)

            left = left.next
            right = right.next

        assert isinstance(left, ListNode)
        assert isinstance(left.next, ListNode)

        left.next = left.next.next
        return dummy.next
