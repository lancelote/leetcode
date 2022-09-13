import copy


class Solution:
    def combinationSum(
        self, candidates: list[int], target: int
    ) -> list[list[int]]:
        combinations: list[list[int]] = []

        def dfs(start: int, total: int, path: list[int]) -> None:
            total += candidates[start]
            path.append(candidates[start])

            if total > target:
                return

            if total == target:
                combinations.append(copy.copy(path))
                return

            for i in range(start, len(candidates)):
                dfs(i, total, path)
                path.pop()

        for start_idx in range(len(candidates)):
            dfs(start_idx, 0, [])

        return combinations
