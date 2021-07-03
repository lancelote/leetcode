class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        assert len(nums) >= 4

        y, z, *_, w, x = sorted(nums)
        return w * x - y * z
