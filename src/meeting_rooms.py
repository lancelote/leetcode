class Interval(object):
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Solution:
    def can_attend_meetings(self, intervals: list[Interval]) -> bool:
        n = len(intervals)
        intervals = sorted(intervals, key=lambda x: x.start)

        for i in range(1, n):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True
