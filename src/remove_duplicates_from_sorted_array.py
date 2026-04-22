class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write_idx = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_idx] = nums[i]
                write_idx += 1

        return write_idx
