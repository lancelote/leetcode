from src.utils.linked_list import ListNode


class Solution:
    def mergeTwoLists(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = current = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next

            current.next = node
            current = node

        while l1:
            node = ListNode(l1.val)
            current.next = node
            current = node
            l1 = l1.next

        while l2:
            node = ListNode(l2.val)
            current.next = node
            current = node
            l2 = l2.next

        return dummy.next
