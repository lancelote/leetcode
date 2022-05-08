import math


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack: list[int] = []
        third = -math.inf

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < third:
                return True
            while stack and nums[i] > stack[-1]:
                third = stack.pop()
            stack.append(nums[i])

        return False
