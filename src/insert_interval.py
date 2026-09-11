class Solution:
    def insert(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        n = len(intervals)

        result: list[list[int]] = []
        new_start, new_end = new_interval

        for i, interval in enumerate(intervals):
            start, end = interval

            # new is before
            if new_end < start:
                result.append([new_start, new_end])
                result.extend(intervals[i] for i in range(i, n))
                return result

            # new is after
            elif new_start > end:
                result.append(interval)

            # new overlaps
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        result.append([new_start, new_end])

        return result
