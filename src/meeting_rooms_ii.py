import heapq


class Interval(object):
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end


class Solution:
    def min_meeting_rooms(self, intervals: list[Interval]) -> int:
        max_rooms = 0
        count = 0

        intervals = sorted(intervals, key=lambda x: x.start)
        starts = [x.start for x in intervals]
        ends: list[int] = []

        for x in intervals:
            heapq.heappush(ends, x.end)

        for start in starts:
            count += 1
            while ends and ends[0] <= start:
                count -= 1
                heapq.heappop(ends)

            max_rooms = max(max_rooms, count)

        return max_rooms
