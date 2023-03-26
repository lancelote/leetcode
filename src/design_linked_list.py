class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Node | None = None
        self.prev: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.val})"


class MyLinkedList:
    def __init__(self) -> None:
        # dummies
        self.head: Node = Node(-1)
        self.tail: Node = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        assert index >= 0

        node = self.head.next

        while node and index:
            node = node.next
            index -= 1

        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        prev_node = self.head
        next_node = self.head.next

        assert prev_node
        assert next_node

        next_node.prev = new_node
        new_node.next = next_node
        prev_node.next = new_node
        new_node.prev = prev_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        prev_node = self.tail.prev
        next_node = self.tail

        assert prev_node
        assert next_node

        next_node.prev = new_node
        new_node.next = next_node
        prev_node.next = new_node
        new_node.prev = prev_node

    def addAtIndex(self, index: int, val: int) -> None:
        assert index >= 0

        node = self.head.next

        while node and index:
            node = node.next
            index -= 1

        if not node:
            return

        new_node = Node(val)
        prev_node = node.prev
        next_node = node

        assert prev_node
        assert next_node

        next_node.prev = new_node
        new_node.next = next_node
        prev_node.next = new_node
        new_node.prev = prev_node

    def deleteAtIndex(self, index: int) -> None:
        assert index >= 0

        node = self.head.next

        while node and index:
            node = node.next
            index -= 1

        if not node or node is self.tail:
            return

        prev_node = node.prev
        next_node = node.next

        assert prev_node
        assert next_node

        prev_node.next = next_node
        next_node.prev = prev_node
