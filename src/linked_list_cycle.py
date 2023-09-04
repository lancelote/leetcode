from src.utils.linked_list import ListNode


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = fast = head

        while slow and fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False
