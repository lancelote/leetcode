class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack: list[str] = []
        result: list[str] = []

        def dfs(start: int, end: int) -> None:
            if start == end == n:
                result.append("".join(stack))
                return

            if start < n:
                stack.append("(")
                dfs(start + 1, end)
                stack.pop()

            if start != end:
                stack.append(")")
                dfs(start, end + 1)
                stack.pop()

        dfs(0, 0)
        return result
