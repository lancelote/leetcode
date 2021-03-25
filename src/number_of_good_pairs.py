from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """A pair (i,j) is called good if nums[i] == nums[j] and i < j."""
        good_pairs = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    good_pairs += 1

        return good_pairs
