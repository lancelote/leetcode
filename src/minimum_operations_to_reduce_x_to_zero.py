class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x

        left = 0
        curr_sum = 0
        longest_window = -1

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                longest_window = max(longest_window, right - left + 1)

        return n - longest_window if longest_window != -1 else -1
