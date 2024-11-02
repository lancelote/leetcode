from src.utils.linked_list import ListNode


class Solution:
    def removeNthFromEnd(
        self, head: ListNode | None, n: int
    ) -> ListNode | None:
        dummy = ListNode(next=head)
        slow = fast = dummy

        for _ in range(n):
            assert fast.next

            fast = fast.next

        while fast.next:
            assert fast.next and slow.next

            fast = fast.next
            slow = slow.next

        assert slow.next
        slow.next = slow.next.next
        return dummy.next
