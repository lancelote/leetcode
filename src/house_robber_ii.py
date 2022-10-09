class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_subarray(start: int, stop: int) -> int:
            rob1 = 0
            rob2 = 0

            for i in range(start, stop):
                tmp = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = tmp

            return rob2

        return max(rob_subarray(0, n - 1), rob_subarray(1, n))
