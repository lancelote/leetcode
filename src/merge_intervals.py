class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        assert intervals

        n = len(intervals)
        result: list[list[int]] = []
        intervals = sorted(intervals, key=lambda x: x[0])

        tmp_start, tmp_end = intervals[0]

        for i in range(1, n):
            start, end = intervals[i]

            if start <= tmp_end:
                tmp_end = max(end, tmp_end)
            else:
                result.append([tmp_start, tmp_end])
                tmp_start = start
                tmp_end = end

        result.append([tmp_start, tmp_end])
        return result
