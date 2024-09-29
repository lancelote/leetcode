class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        current_sum = 0
        min_len = len(nums)
        left, right = 0, 0

        while right < len(nums):
            current_sum += nums[right]
            right += 1

            while current_sum > target and current_sum - nums[left] >= target:
                current_sum -= nums[left]
                left += 1

            if current_sum >= target:
                min_len = min(min_len, right - left)

        return min_len if current_sum >= target else 0
