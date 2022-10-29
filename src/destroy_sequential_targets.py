import sys


class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        reminders: dict[int, tuple[int, int]] = {}
        max_destroyed = 0

        for num in nums:
            reminder = num % space

            if reminder in reminders:
                count, min_val = reminders[reminder]
                reminders[reminder] = (count + 1, min(min_val, num))
            else:
                reminders[reminder] = (1, num)

            max_destroyed = max(max_destroyed, reminders[reminder][0])

        min_val = sys.maxsize

        for _, (destroyed, val) in reminders.items():
            if destroyed == max_destroyed:
                min_val = min(min_val, val)

        return min_val
