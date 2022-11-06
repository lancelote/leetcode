from src.utils.linked_list import ListNode


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        next_node = node.next
        assert next_node

        node.val = next_node.val
        node.next = next_node.next
        del next_node
