class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = [0] * (2 * n)

        for i in range(n):
            result[i * 2] = nums[i]

        for i in range(n, 2 * n):
            result[(i - n) * 2 + 1] = nums[i]

        return result
