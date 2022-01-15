class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            middle_index = left_index + (right_index - left_index) // 2
            middle_value = nums[middle_index]

            if middle_value == target:
                return middle_index
            elif middle_value > target:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1

        return -1
