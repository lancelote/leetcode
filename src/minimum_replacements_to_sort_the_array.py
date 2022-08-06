import math


class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        replacements = 0
        limit = nums[-1]

        for x in reversed(nums):
            if x > limit:
                new_numbers = math.ceil(x / limit)
                replacements += new_numbers - 1
                limit = x // new_numbers
            else:
                limit = x

        return replacements
