from functools import cache


class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        @cache
        def dp(i1: int, i2: int) -> int:
            if i1 == len(nums1) or i2 == len(nums2):
                return 0

            take = nums1[i1] * nums2[i2] + dp(i1 + 1, i2 + 1)
            return max(take, dp(i1 + 1, i2), dp(i1, i2 + 1))

        if max(nums1) < 0 < min(nums2):
            return max(nums1) * min(nums2)
        if max(nums2) < 0 < min(nums1):
            return max(nums2) * min(nums1)

        return dp(0, 0)
