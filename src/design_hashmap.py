class Pair:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.next: Pair | None = None


class MyHashMap:
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 2
        self.data: list[Pair | None] = [None, None]

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        pair = self.data[index]

        if pair:
            while pair.key != key and pair.next:
                pair = pair.next

            if pair.key == key:
                pair.val = value
            else:
                pair.next = Pair(key, value)
                self.size += 1
        else:
            self.data[index] = Pair(key, value)
            self.size += 1

        if self.size >= self.capacity // 2:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash(key)
        pair = self.data[index]

        while pair and pair.key != key:
            pair = pair.next

        return pair.val if pair else -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        pair = self.data[index]

        # start of the chain
        if pair and pair.key == key:
            self.data[index] = pair.next
            self.size -= 1
            return

        # middle/end of the chain
        while pair and pair.next:
            if pair.next.key == key:
                pair.next = pair.next.next
                self.size -= 1
                return
            pair = pair.next

    def hash(self, key: int) -> int:
        return key % self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        old_data = self.data
        self.data = [None] * self.capacity

        for x in old_data:
            while x:
                self.put(x.key, x.val)
                x = x.next
