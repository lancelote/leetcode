class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window = 0
        for i in range(k):
            window += nums[i]

        max_window = window

        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            max_window = max(max_window, window)

        return max_window / k
