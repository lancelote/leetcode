class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            middle = (right - left) // 2 + left
            guess = nums[middle]

            if guess == target:
                return middle
            elif guess < target:
                left = middle + 1
            else:
                right = middle

        return -1
