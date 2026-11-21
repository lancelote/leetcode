from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result: list[int] = []
        count2 = Counter(nums2)

        for x in nums1:
            if count2[x] > 0:
                count2[x] -= 1
                result.append(x)

        return result
