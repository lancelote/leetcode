from src.utils.linked_list import ListNode


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        assert head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        assert slow

        # reverse
        second = slow.next
        slow.next = None  # detach first part
        prev: ListNode | None = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge
        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
