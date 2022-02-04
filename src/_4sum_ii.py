from collections import defaultdict


class Solution:
    def fourSumCount(
        self,
        nums1: list[int],
        nums2: list[int],
        nums3: list[int],
        nums4: list[int],
    ) -> int:
        sums: dict[int, int] = defaultdict(int)
        result = 0
        n = len(nums1)

        for i in range(n):
            for j in range(n):
                sums[nums1[i] + nums2[j]] += 1

        for k in range(n):
            for m in range(n):
                result += sums[0 - (nums3[k] + nums4[m])]

        return result
