from functools import cache


class Solution:
    def minimizeConcatenatedLength(self, words: list[str]) -> int:
        @cache
        def dfs(i: int, left: str, right: str) -> int:
            if i == len(words):
                return 0

            to_left = dfs(
                i + 1,
                words[i][0],
                right,
            ) - (words[i][-1] == left)

            to_right = dfs(
                i + 1,
                left,
                words[i][-1],
            ) - (words[i][0] == right)

            return min(to_left, to_right) + len(words[i])

        return dfs(1, words[0][0], words[0][-1]) + len(words[0])
