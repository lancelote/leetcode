from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = Counter(nums)
        return sum(x * (x - 1) // 2 for x in count.values())
