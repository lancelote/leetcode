class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0

        for i, x in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + x)

        return max_reach >= len(nums) - 1
