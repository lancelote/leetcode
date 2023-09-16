class Solution:
    def minimumRightShifts(self, nums: list[int]) -> int:
        n = len(nums)

        first_small = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                first_small = i
                break

        if not first_small:
            return 0

        for i in range(first_small, n):
            if nums[i] > nums[0]:
                return -1

        for i in range(first_small + 1, n):
            if nums[i - 1] > nums[i]:
                return -1

        return n - first_small
