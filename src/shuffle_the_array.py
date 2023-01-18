class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        assert len(nums) == n * 2, "Unexpected array length"

        result = []

        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])

        return result
