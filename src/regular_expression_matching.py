class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache: dict[tuple[int, int], bool] = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= len(s) and j >= len(p):
                result = True
            elif i >= len(s) and j < len(p) - 1 and p[j + 1] == "*":
                result = dfs(i, j + 2)
            elif i == len(s) or j == len(p):
                result = False
            elif j < len(p) - 1 and p[j + 1] == "*":
                if s[i] == p[j] or p[j] == ".":
                    result = dfs(i + 1, j) or dfs(i, j + 2)
                else:
                    result = dfs(i, j + 2)
            elif p[j] == ".":
                result = dfs(i + 1, j + 1)
            elif s[i] != p[j]:
                result = False
            else:
                result = dfs(i + 1, j + 1)

            cache[(i, j)] = result
            return result

        return dfs(0, 0)
