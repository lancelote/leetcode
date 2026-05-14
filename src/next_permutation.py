class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)

        self.reverse(nums, i + 1)

    def swap(self, nums: list[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]

    def reverse(self, nums, start) -> None:
        left, right = start, len(nums) - 1
        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1
