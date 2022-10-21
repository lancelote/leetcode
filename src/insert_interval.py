class Solution:
    def insert(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        n = len(intervals)
        new_start, new_end = new_interval
        result: list[list[int]] = []

        for i, [start, end] in enumerate(intervals):
            if end < new_start:
                result.append([start, end])
            elif start > new_end:
                result.append([new_start, new_end])
                result.extend(intervals[j] for j in range(i, n))
                return result
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)

        result.append([new_start, new_end])
        return result
