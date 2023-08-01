class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        cache: dict[tuple[int, int, int], int] = {}

        def dfs(i: int, zeros_left: int, ones_left: int) -> int:
            if i == len(strs):
                return 0
            if (i, zeros_left, ones_left) in cache:
                return cache[(i, zeros_left, ones_left)]

            word = strs[i]
            zeros, ones = word.count("0"), word.count("1")
            new_zeros, new_ones = zeros_left - zeros, ones_left - ones

            cache[(i, zeros_left, ones_left)] = dfs(
                i + 1, zeros_left, ones_left
            )

            if new_zeros >= 0 and new_ones >= 0:
                cache[(i, zeros_left, ones_left)] = max(
                    cache[(i, zeros_left, ones_left)],
                    1 + dfs(i + 1, new_zeros, new_ones),
                )
            return cache[(i, zeros_left, ones_left)]

        return dfs(0, m, n)
