from src.utils.linked_list import ListNode


class Solution:
    def removeNthFromEnd(
        self, head: ListNode | None, n: int
    ) -> ListNode | None:
        dummy = ListNode(next=head)
        left: ListNode | None = dummy
        right: ListNode | None = head

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
