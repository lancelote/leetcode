class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result: list[int] = []

        left = 0
        right = sum(nums)

        for i, x in enumerate(nums):
            to_left = x * i - left
            to_right = right - x * (n - i)

            result.append(to_left + to_right)

            left += x
            right -= x

        return result
