from functools import reduce
from itertools import chain
from itertools import combinations
from operator import xor


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        result = 0

        subsets = (combinations(nums, r) for r in range(len(nums) + 1))
        for subset in chain.from_iterable(subsets):
            result += reduce(xor, subset, 0)

        return result
