import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.left_limit = 1
        self.added_back_heap: list[int] = []
        self.added_back_set: set[int] = set()

    def popSmallest(self) -> int:
        if self.added_back_set:
            smallest = heapq.heappop(self.added_back_heap)
            self.added_back_set.remove(smallest)
        else:
            smallest = self.left_limit
            self.left_limit += 1

        return smallest

    def addBack(self, num: int) -> None:
        if num >= self.left_limit:
            return

        if num in self.added_back_set:
            return

        heapq.heappush(self.added_back_heap, num)
        self.added_back_set.add(num)
