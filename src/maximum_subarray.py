class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        current_sum = max_sum = nums[0]

        for i in range(1, n):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
