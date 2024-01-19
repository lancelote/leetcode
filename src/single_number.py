from functools import reduce


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
