class Removed:
    pass


DELETED = Removed()


class MyHashSet:
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 2
        self.data: list[int | None | Removed] = [None, None]

    def add(self, key: int) -> None:
        index = self.hash(key)

        while self.data[index] is not None:
            if self.data[index] == key:
                return

            index += 1
            index %= self.capacity

        self.data[index] = key
        self.size += 1

        if self.size >= self.capacity // 2:
            self.resize()

    def remove(self, key: int) -> None:
        index = self.hash(key)

        while self.data[index] is not None:
            if self.data[index] == key:
                self.data[index] = DELETED
                return
            else:
                index += 1
                index %= self.capacity

    def contains(self, key: int) -> bool:
        index = self.hash(key)

        while self.data[index] is not None:
            if self.data[index] == key:
                return True
            else:
                index += 1
                index %= self.capacity

        return False

    def hash(self, key: int) -> int:
        return key % self.capacity

    def resize(self) -> None:
        self.size = 0
        self.capacity *= 2
        old_data = self.data
        self.data = [None] * self.capacity

        for x in old_data:
            if isinstance(x, int):
                self.add(x)
