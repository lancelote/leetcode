class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        i = 1
        count = 1

        jump = nums[0]

        while jump < len(nums) - 1:
            next_jump = 0

            while i <= jump and i < len(nums):
                next_jump = max(next_jump, nums[i] + i)
                i += 1

            jump = next_jump
            count += 1

        return count
