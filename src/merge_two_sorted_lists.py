from src.utils.linked_list import ListNode


class Solution:
    def mergeTwoLists(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode()
        head = dummy

        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                head = l2
                l2 = l2.next
            else:
                head.next = l1
                head = l1
                l1 = l1.next

        while l1:
            head.next = l1
            head = l1
            l1 = l1.next

        while l2:
            head.next = l2
            head = l2
            l2 = l2.next

        return dummy.next
