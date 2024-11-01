from src.utils.linked_list import ListNode


class Solution:
    def reverseBetween(
        self,
        head: ListNode | None,
        left: int,
        right: int,
    ) -> ListNode | None:
        dummy = prev = ListNode(-1, next=head)

        # skip left
        for _ in range(left - 1):
            assert prev and prev.next
            prev = prev.next

        assert prev.next
        start = prev
        prev = prev.next
        current = prev.next

        # revert till right
        for _ in range(right - left):
            assert current
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        end = current
        tmp = start.next
        start.next = prev
        assert tmp
        tmp.next = end

        return dummy.next
