from collections import defaultdict


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        count = 0
        diff: dict[int, int] = defaultdict(int)

        for x in nums:
            if diff[x]:
                diff[x] -= 1
                count += 1
            else:
                diff[k - x] += 1

        return count
