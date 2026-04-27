from src.utils.linked_list import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = current = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1 and l2:
                new_val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                new_val = l1.val + carry
                l1 = l1.next
            elif l2:
                new_val = l2.val + carry
                l2 = l2.next
            else:
                new_val = carry

            current.next = ListNode(new_val % 10)
            carry = new_val // 10
            current = current.next

        return dummy.next
