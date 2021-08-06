class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        to_insert = 0

        for num in nums:
            if num != val:
                nums[to_insert] = num
                to_insert += 1

        return to_insert
