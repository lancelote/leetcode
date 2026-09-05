class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result: list[list[int]] = []

        def backtrack(start: int) -> None:
            if start == n:
                result.append(nums[::])
                return

            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]

        backtrack(0)
        return result
