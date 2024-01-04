import heapq


class SmallestInfiniteSet:
    def __init__(self) -> None:
        self.h: list[int] = []
        self.added_back: set[int] = set()
        self.top = 1

    def popSmallest(self) -> int:
        if self.h:
            pop = heapq.heappop(self.h)
        else:
            pop = self.top
            self.top += 1

        self.added_back.discard(pop)
        return pop

    def addBack(self, num: int) -> None:
        if num < self.top and num not in self.added_back:
            self.added_back.add(num)
            heapq.heappush(self.h, num)
