class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n = len(intervals)
        sorted_intervals = sorted(intervals)
        result: list[list[int]] = [sorted_intervals[0]]

        for i in range(1, n):
            left, right = sorted_intervals[i]

            if result[-1][1] >= left:
                result[-1][1] = max(result[-1][1], right)
            else:
                result.append([left, right])

        return result
