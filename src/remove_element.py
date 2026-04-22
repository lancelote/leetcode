class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write_idx = 0

        for i, x in enumerate(nums):
            if x != val:
                nums[write_idx] = x
                write_idx += 1

        return write_idx
