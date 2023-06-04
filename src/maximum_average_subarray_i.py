class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        running_sum = 0

        for i in range(k):
            running_sum += nums[i]

        max_average = running_sum / k

        for i in range(k, len(nums)):
            running_sum += nums[i] - nums[i - k]
            current_average = running_sum / k
            max_average = max(max_average, current_average)

        return max_average
