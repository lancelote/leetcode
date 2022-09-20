class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        cache = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    cache[i][j] = cache[i + 1][j + 1] + 1

        return max(max(row) for row in cache)
