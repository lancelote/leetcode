from src.utils.linked_list import ListNode


def get_length(head: ListNode | None) -> int:
    result = 0

    while head:
        result += 1
        head = head.next

    return result


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        n = get_length(head)

        if n == 0 or n == 1:
            return head

        k = k % n
        if k == 0:
            return head

        dummy = left = ListNode(next=head)

        for _ in range(n - k):
            assert left.next
            left = left.next

        new_start = left.next

        last = left
        while last and last.next:
            last = last.next

        dummy.next = new_start
        last.next = head
        left.next = None
        return dummy.next
