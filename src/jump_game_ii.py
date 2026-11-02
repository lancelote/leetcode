class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        answer = 0
        end, far = 0, 0

        for i in range(n - 1):
            far = max(far, i + nums[i])

            if i == end:
                answer += 1
                end = far

        return answer
