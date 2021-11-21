class Solution:
    def minOperations(self, nums: list[int]) -> int:
        assert len(nums) > 0

        operations = 0
        previous = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]

            if current <= previous:
                operations += previous - current + 1
                previous = previous + 1
            else:
                previous = current

        return operations
