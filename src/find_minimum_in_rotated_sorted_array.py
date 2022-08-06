class Solution:
    def findMin(self, nums: list[int]) -> int:
        assert nums

        smallest = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                smallest = min(smallest, nums[left])
                break

            middle = (left + right) // 2

            if nums[middle] >= smallest:
                left = middle + 1
            else:
                smallest = nums[middle]
                right = middle - 1

        return smallest
