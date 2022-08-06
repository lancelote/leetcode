from src.utils.linked_list import ListNode


class Solution:
    def mergeTwoLists(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        if not l1:
            return l2
        if not l2:
            return l1
        elif l1.val > l2.val:
            return ListNode(l2.val, next=self.mergeTwoLists(l1, l2.next))
        else:
            return ListNode(l1.val, next=self.mergeTwoLists(l1.next, l2))
