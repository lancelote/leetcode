import random


class RandomizedSet:
    def __init__(self) -> None:
        self.itemToIdx: dict[int, int] = {}
        self.items: list[int] = []

    def insert(self, val: int) -> bool:
        if val in self.itemToIdx:
            return False

        self.items.append(val)
        self.itemToIdx[val] = len(self.items) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.itemToIdx:
            return False

        idx = self.itemToIdx.pop(val)
        last_item = self.items.pop()

        if self.items and last_item != val:
            self.items[idx] = last_item
            self.itemToIdx[last_item] = idx

        return True

    def getRandom(self) -> int:
        random_idx = random.randint(0, len(self.items) - 1)
        return self.items[random_idx]
