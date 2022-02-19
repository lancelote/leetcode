class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        biggest_sum = nums[0]
        current_sum = 0

        for num in nums:
            if current_sum < 0:
                current_sum = num
            else:
                current_sum += num
            biggest_sum = max(biggest_sum, current_sum)

        return biggest_sum
