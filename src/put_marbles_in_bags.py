import heapq


class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        min_heap: list[int] = []
        max_heap: list[int] = []

        for i in range(len(weights) - 1):
            a, b = weights[i], weights[i + 1]
            heapq.heappush(min_heap, a + b)
            heapq.heappush(max_heap, -a - b)

        min_sum = max_sum = weights[0] + weights[-1]

        for _ in range(k - 1):
            min_sum += heapq.heappop(min_heap)
            max_sum -= heapq.heappop(max_heap)

        return max_sum - min_sum
