class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 1

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            nums[j] = nums[i]
            j += 1

        return j
