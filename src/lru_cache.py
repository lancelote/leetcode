class Node:
    def __init__(
        self,
        key: int,
        val: int,
        next_node: Node | None = None,
        prev_node: Node | None = None,
    ) -> None:
        self.key = key
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self) -> str:
        return f"Node(key={self.key}, val={self.val})"


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.key_to_node: dict[int, Node] = {}

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next_node = self.tail
        self.tail.prev_node = self.head

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]

        self.cut(node)
        self.append_left(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            existing_node = self.key_to_node[key]
            self.cut(existing_node)

        new_node = Node(key, value)
        self.append_left(new_node)

    def cut(self, node: Node) -> None:
        assert len(self.key_to_node) > 0

        prev_node = node.prev_node
        next_node = node.next_node

        assert prev_node is not None
        assert next_node is not None

        prev_node.next_node = next_node
        next_node.prev_node = prev_node

        node.prev_node = None
        node.next_node = None

        del self.key_to_node[node.key]

    def append_left(self, node: Node) -> None:
        old_first = self.head.next_node

        assert old_first is not None

        self.head.next_node = node
        node.next_node = old_first
        old_first.prev_node = node
        node.prev_node = self.head

        self.key_to_node[node.key] = node

        if len(self.key_to_node) > self.capacity:
            self.pop()

    def pop(self) -> None:
        assert len(self.key_to_node) > 0

        node_to_remove = self.tail.prev_node

        assert node_to_remove is not None

        self.cut(node_to_remove)
