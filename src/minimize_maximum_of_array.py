import math


class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        cum_sum = maximum = 0

        for i, num in enumerate(nums, start=1):
            cum_sum += num
            maximum = max(math.ceil(cum_sum / i), maximum)

        return maximum
