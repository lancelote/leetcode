import typing
from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        good_paris = 0
        diffs: typing.DefaultDict[int, int] = defaultdict(int)

        for i, x in enumerate(nums):
            diffs[i - x] += 1

        for v in diffs.values():
            good_paris += v * (v - 1) // 2

        n = len(nums)
        return n * (n - 1) // 2 - good_paris
