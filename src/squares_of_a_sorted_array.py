class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left_index = 0
        right_index = len(nums) - 1
        result = []

        while left_index <= right_index:
            left_value = nums[left_index]
            right_value = nums[right_index]

            if abs(left_value) > abs(right_value):
                left_index += 1
                result.append(left_value * left_value)
            else:
                right_index -= 1
                result.append(right_value * right_value)

        return result[::-1]
