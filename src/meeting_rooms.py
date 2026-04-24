class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        prev_end = -1
        for start, end in sorted(intervals):
            if start < prev_end:
                return False
            prev_end = end
        return True
