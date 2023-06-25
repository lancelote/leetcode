class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_length = 0
        replace = 1
        left = 0

        for right, num in enumerate(nums):
            if num == 1:
                pass
            elif replace:
                replace -= 1
            else:
                while nums[left] != 0:
                    left += 1
                left += 1
            max_length = max(right - left + 1 - (replace == 0), max_length)

        return max_length - replace
