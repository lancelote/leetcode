class Node:
    def __init__(self, key: int = -1, val: int = -1) -> None:
        self.key = key
        self.val = val
        self.next: Node | None = None


class MyHashMap:
    def __init__(self) -> None:
        self.data = [Node()] * 1000

    def put(self, key: int, value: int) -> None:
        current: Node | None = self.data[key % 1000]

        while current:
            if current.key == key:
                current.val = value
                return

            current = current.next

        new_node = Node(key, value)
        new_node.next = self.data[key % 1000]
        self.data[key % 1000] = new_node

    def get(self, key: int) -> int:
        node = self.data[key % 1000]

        while node.key != key and node.key != -1:
            assert node.next
            node = node.next

        return node.val

    def remove(self, key: int) -> None:
        dummy = Node()
        dummy.next = self.data[key % 1000]
        current = dummy

        assert current.next
        while current.next.key != key and current.next.key != -1:
            current = current.next

        assert current.next
        if current.next.key == key:
            current.next = current.next.next
            self.data[key % 1000] = dummy.next
