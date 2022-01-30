class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        result = []

        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                result.append(nums[right] ** 2)
                right -= 1
            else:
                result.append(nums[left] ** 2)
                left += 1

        return result[::-1]
