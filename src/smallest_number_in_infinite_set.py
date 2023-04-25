import heapq


class SmallestInfiniteSet:
    def __init__(self) -> None:
        self.smallest_limit = 1
        self.smallest_heap: list[int] = []
        self.smallest_heap_set: set[int] = set()

    def popSmallest(self) -> int:
        if self.smallest_heap:
            x = heapq.heappop(self.smallest_heap)
            self.smallest_heap_set.remove(x)
        else:
            x = self.smallest_limit
            self.smallest_limit += 1
        return x

    def addBack(self, num: int) -> None:
        if num < self.smallest_limit and num not in self.smallest_heap_set:
            heapq.heappush(self.smallest_heap, num)
            self.smallest_heap_set.add(num)
