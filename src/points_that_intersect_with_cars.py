class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        nums.sort()

        a, b = nums[0]
        total = b - a + 1
        for i in range(1, len(nums)):
            na, nb = nums[i]
            total += max(b, nb) + 1 - max(b + 1, na)
            b = max(b, nb)

        return total
