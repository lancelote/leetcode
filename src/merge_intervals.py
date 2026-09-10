class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result: list[list[int]] = []

        intervals.sort()
        last_start, last_end = intervals[0]

        for start, end in intervals:
            if start <= last_end:
                last_end = max(end, last_end)
            else:
                result.append([last_start, last_end])
                last_start, last_end = start, end

        result.append([last_start, last_end])

        return result
