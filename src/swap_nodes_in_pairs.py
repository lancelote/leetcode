from src.utils.linked_list import ListNode


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy_odd = odd = ListNode(-1)
        dummy_even = even = ListNode(-1)

        while head:
            odd.next = head
            odd = odd.next
            head = head.next

            if head:
                even.next = head
                even = even.next
                head = head.next

        odd.next = None
        even.next = None

        odd = dummy_odd.next
        even = dummy_even.next

        dummy = ListNode(-1)
        current = dummy

        while odd:
            if even:
                current.next = even
                current = current.next
                even = even.next

            current.next = odd
            current = current.next
            odd = odd.next

        return dummy.next
