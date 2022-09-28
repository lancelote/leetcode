from src.utils.linked_list import ListNode


class Solution:
    def removeNthFromEnd(
        self, head: ListNode | None, n: int
    ) -> ListNode | None:
        dummy = ListNode(next=head)
        slow, fast = dummy, dummy

        for _ in range(n):
            assert fast.next
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
