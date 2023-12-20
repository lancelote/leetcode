import heapq


class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        h: list[int] = []

        for x in prices:
            heapq.heappush(h, -x)
            if len(h) > 2:
                heapq.heappop(h)

        total = money + sum(h)
        return total if total >= 0 else money
