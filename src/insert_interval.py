class Solution:
    def insert(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        n = len(intervals)
        result: list[list[int]] = []

        new_start, new_end = new_interval

        for i, interval in enumerate(intervals):
            start, end = interval

            # interval before the new one
            if end < new_start:
                result.append(interval)

            # interval after the new one
            elif start > new_end:
                result.append([new_start, new_end])
                result.extend(intervals[j] for j in range(i, n))
                return result

            # collision
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        result.append([new_start, new_end])
        return result
