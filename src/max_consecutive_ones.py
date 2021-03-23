from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        longest_streak = 0

        for num in nums:
            if num:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 0

        return max(longest_streak, current_streak)
