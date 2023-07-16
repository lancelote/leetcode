from src.utils.linked_list import ListNode


class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        current_odd = odd_dummy = ListNode(-1)
        current_even = even_dummy = ListNode(-1)

        current_odd.next = even_dummy.next

        i = 1
        while head:
            if i % 2 == 1:
                current_odd.next = head
                current_odd = head
            else:
                current_even.next = head
                current_even = head
            head = head.next
            i += 1

        current_even.next = None
        current_odd.next = even_dummy.next
        return odd_dummy.next
