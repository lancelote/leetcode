class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result: list[int] = []

        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] * nums[left])
                left += 1
            else:
                result.append(nums[right] * nums[right])
                right -= 1

        return result[::-1]
