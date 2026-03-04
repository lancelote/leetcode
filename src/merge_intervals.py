class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals)
        result: list[list[int]] = []

        start, stop = intervals[0]
        for i in range(1, len(intervals)):
            next_start, next_stop = intervals[i]

            if next_start <= stop:
                stop = max(stop, next_stop)
            else:
                result.append([start, stop])
                start = next_start
                stop = next_stop

        result.append([start, stop])
        return result
