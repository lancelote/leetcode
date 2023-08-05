from math import gcd

from src.utils.linked_list import ListNode


class Solution:
    def insertGreatestCommonDivisors(
        self, head: ListNode | None
    ) -> ListNode | None:
        if not head or not head.next:
            return head

        a: ListNode | None = head
        b: ListNode | None = head.next

        while b:
            assert a and b

            c = ListNode(val=gcd(a.val, b.val))
            a.next = c
            c.next = b

            a, b = b, b.next

        return head
