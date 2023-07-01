class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            left_sum += num
            if left_sum == right_sum:
                return i
            right_sum -= num

        return -1
