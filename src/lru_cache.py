class Node:
    def __init__(self, val: int, key: int) -> None:
        self.val = val
        self.key = key

        self.nxt: Node | None = None
        self.prv: Node | None = None

    def __str__(self) -> str:
        return f"Node(val={self.val}, key={self.key})"


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.n = capacity

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.nxt = self.tail
        self.tail.prv = self.head

        self.cache: dict[int, Node] = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.touch(node)
            return node.val
        else:
            return -1

    def touch(self, node: Node | None) -> None:
        self.cut(node)
        self.append(node)

    def append(self, node: Node | None) -> None:
        assert node

        prv = self.tail.prv
        assert prv
        prv.nxt = node
        node.nxt = self.tail
        self.tail.prv = node
        node.prv = prv

    @staticmethod
    def cut(node: Node | None) -> None:
        assert node

        prv = node.prv
        nxt = node.nxt
        assert prv and nxt
        prv.nxt = nxt
        nxt.prv = prv

    def pop_left(self) -> None:
        if self.head.nxt is not self.tail:
            node = self.head.nxt
            self.cut(node)
            assert node
            del self.cache[node.key]

    def put(self, key: int, value: int) -> None:
        # existing key, update
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.touch(node)

        # new key, free space available
        elif self.n:
            node = Node(value, key)
            self.append(node)
            self.cache[key] = node
            self.n -= 1

        # new key, no free space
        else:
            node = Node(value, key)
            self.pop_left()
            self.append(node)
            self.cache[key] = node
