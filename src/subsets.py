class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        current: list[int] = []

        def dfs(i: int = 0) -> None:
            if i == len(nums):
                result.append(current.copy())
                return

            dfs(i + 1)
            current.append(nums[i])
            dfs(i + 1)
            current.pop()

        dfs()
        return result
