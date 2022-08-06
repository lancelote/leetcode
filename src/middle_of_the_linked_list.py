from src.utils.linked_list import ListNode


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow, fast = head, head

        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
