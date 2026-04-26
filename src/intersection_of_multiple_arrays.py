class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        n = len(nums)
        counts = [0] * 1001

        for sub_array in nums:
            for x in sub_array:
                counts[x] += 1

        return [i for i, x in enumerate(counts) if x == n]
