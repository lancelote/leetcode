from typing import Optional

OptNode = Optional["ListNode"]


class ListNode:
    def __init__(self, val: int = 0, next: OptNode = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: OptNode) -> OptNode:
        slow, fast = head, head

        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
