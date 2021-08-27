from math import gcd


class Solution:
    def findGCD(self, nums: list[int]) -> int:
        return gcd(min(nums), max(nums))
