import heapq


class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        n = len(piles) // 3
        heap = [-x for x in piles]
        heapq.heapify(heap)
        result = 0

        for _ in range(n):
            heapq.heappop(heap)
            result -= heapq.heappop(heap)

        return result
