class Solution:
    def combinationSum(
        self, candidates: list[int], target: int
    ) -> list[list[int]]:
        result: list[list[int]] = []
        current: list[int] = []

        def dfs(candidate_idx: int = 0, sum_so_far: int = 0) -> None:
            if candidate_idx >= len(candidates):
                return

            if sum_so_far > target:
                return

            if sum_so_far == target:
                result.append(current[::])
                return

            # add once again
            candidate = candidates[candidate_idx]
            current.append(candidate)
            dfs(candidate_idx, sum_so_far + candidate)
            current.pop()

            # move forward
            dfs(candidate_idx + 1, sum_so_far)

        dfs()
        return result
