class Solution:
    def findMin(self, nums: list[int]) -> int:
        assert len(nums) != 0

        left, right = 0, len(nums) - 1
        min_value = nums[0]

        while left <= right:
            middle = left + (right - left) // 2
            guess = nums[middle]

            if guess >= min_value:
                left = middle + 1
            else:
                min_value = guess
                right = middle - 1

        return min_value
