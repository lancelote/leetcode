from collections import defaultdict
from typing import DefaultDict


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """A pair (i,j) is called good if nums[i] == nums[j] and i < j."""
        good_pairs = 0
        duplicates: DefaultDict[int, int] = defaultdict(int)

        for num in nums:
            good_pairs += duplicates[num]
            duplicates[num] += 1

        return good_pairs
