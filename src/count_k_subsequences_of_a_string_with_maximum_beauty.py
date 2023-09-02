import heapq
import math
from collections import Counter


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        mod = 1_000_000_007
        key_counter = Counter(s)
        value_counter = Counter(key_counter.values())

        heap: list[int] = []

        for v in key_counter.values():
            heapq.heappush(heap, v)

        while len(heap) != k:
            if not heap:
                return 0
            heapq.heappop(heap)

        count = 1
        for x in heap:
            count *= x

        min_values = heap.count(heap[0])
        return count * math.comb(value_counter[heap[0]], min_values) % mod
