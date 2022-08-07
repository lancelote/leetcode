from src.utils.linked_list import ListNode


class Solution:
    def mergeTwoLists(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                tail = l2
                l2 = l2.next
            else:
                tail.next = l1
                tail = l1
                l1 = l1.next

        while l1:
            tail.next = l1
            tail = l1
            l1 = l1.next

        while l2:
            tail.next = l2
            tail = l2
            l2 = l2.next

        return dummy.next
