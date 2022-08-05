class Solution:
    def search(self, nums: list[int], target: int) -> int:
        assert nums

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            guess = nums[middle]
            in_left_portion = guess >= nums[left]
            is_too_small = guess < target
            is_too_big = guess > target

            if guess == target:
                return middle
            elif in_left_portion:
                if is_too_small or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if is_too_big or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1
