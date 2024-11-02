from src.utils.linked_list import ListNode


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy_ls = ls = ListNode()
        dummy_gt = gt = ListNode()

        while head:
            if head.val < x:
                ls.next = head
                ls = ls.next
            else:
                gt.next = head
                gt = gt.next
            head = head.next

        gt.next = None
        ls.next = dummy_gt.next
        return dummy_ls.next
