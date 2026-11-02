class Solution:
    def rob(self, nums: list[int]) -> int:
        rob, dont = 0, 0

        for x in nums:
            rob, dont = max(rob, dont + x), rob

        return max(rob, dont)
