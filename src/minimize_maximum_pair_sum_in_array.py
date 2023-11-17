class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums = sorted(nums)

        max_sum = 0

        left, right = 0, len(nums) - 1

        while left < right:
            max_sum = max(max_sum, nums[left] + nums[right])
            left += 1
            right -= 1

        return max_sum
