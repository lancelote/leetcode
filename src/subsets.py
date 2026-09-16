class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result: list[list[int]] = []
        current: list[int] = []

        def dfs(i: int) -> None:
            if i >= n:
                result.append(current[::])
                return

            dfs(i + 1)
            current.append(nums[i])
            dfs(i + 1)
            current.pop()

        dfs(0)
        return result
