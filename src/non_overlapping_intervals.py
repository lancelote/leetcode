class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        result = 0
        intervals = sorted(intervals, key=lambda x: x[0])
        last_end = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] < last_end:
                last_end = min(last_end, intervals[i][1])
                result += 1
            else:
                last_end = intervals[i][1]

        return result
