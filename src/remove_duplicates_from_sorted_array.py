class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        to_insert = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[to_insert - 1]:
                nums[to_insert] = nums[i]
                to_insert += 1

        return to_insert
