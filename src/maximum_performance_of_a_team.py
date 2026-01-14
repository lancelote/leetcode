import heapq


class Solution:
    def maxPerformance(
        self, _: int, speed: list[int], efficiency: list[int], k: int
    ) -> int:
        max_perf = 0
        speed_sum = 0
        speed_heap: list[int] = []

        engineers = [(e, s) for (e, s) in zip(efficiency, speed)]
        engineers.sort(reverse=True)

        for e, s in engineers:
            if len(speed_heap) == k:
                speed_sum -= heapq.heappop(speed_heap)

            speed_sum += s
            heapq.heappush(speed_heap, s)
            max_perf = max(max_perf, speed_sum * e)

        return max_perf % (10**9 + 7)
