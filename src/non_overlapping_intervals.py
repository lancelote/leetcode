class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        n = len(intervals)
        result = 0
        intervals.sort()

        _, end = intervals[0]

        for i in range(1, n):
            next_start, next_end = intervals[i]

            if next_start < end:
                result += 1

                if next_end < end:
                    end = next_end
            else:
                end = next_end

        return result
