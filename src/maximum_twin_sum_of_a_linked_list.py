from src.utils.linked_list import ListNode


def reverse(head: ListNode | None) -> ListNode | None:
    current: ListNode | None = None

    while head:
        tmp = head.next
        head.next = current
        current = head
        head = tmp

    return current


class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        assert head

        slow: ListNode | None = head
        fast: ListNode | None = head
        left: ListNode | None = head

        while slow and fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        assert slow
        right = reverse(slow.next)
        slow.next = None

        max_sum = 0

        while left and right:
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next

        return max_sum
