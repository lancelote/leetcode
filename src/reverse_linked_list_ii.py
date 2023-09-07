from src.utils.linked_list import ListNode


class Solution:
    def reverseBetween(
        self, head: ListNode | None, left: int, right: int
    ) -> ListNode | None:
        dummy = ListNode(-1, next=head)
        last = dummy

        for _ in range(left - 1):
            assert last and last.next
            last = last.next

        start = last.next
        prev = start
        assert prev
        current = prev.next

        for _ in range(right - left):
            assert current
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        last.next = prev
        assert start
        start.next = current

        return dummy.next
