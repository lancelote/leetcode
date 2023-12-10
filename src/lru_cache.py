class Node:
    def __init__(self, val: int, key: int = -1) -> None:
        self.val = val
        self.key = key

        self.prev: Node | None = None
        self.next: Node | None = None

    def __repr__(self) -> str:
        return f"Node(val={self.val}, key={self.key})"


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: dict[int, Node] = {}

        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def insert_as_head(self, node: Node) -> None:
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

        assert node.next
        node.next.prev = node

    @staticmethod
    def remove(node: Node) -> None:
        assert node.next
        assert node.prev

        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert_as_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
        else:
            node = Node(val=value, key=key)
            self.cache[key] = node
            self.size += 1

            if self.size > self.capacity:
                oldest_node = self.tail.prev
                assert oldest_node
                self.remove(oldest_node)
                del self.cache[oldest_node.key]
                self.size -= 1

        self.insert_as_head(node)
