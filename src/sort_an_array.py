class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            j = i

            while j > 0 and nums[j] < nums[j - 1]:
                tmp = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = tmp
                j -= 1

        return nums
