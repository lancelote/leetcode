class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result: list[str] = []

        current: list[str] = []
        to_open = n

        def dfs() -> None:
            nonlocal n
            nonlocal to_open

            if n == 0:
                result.append("".join(current))
                return

            if to_open != 0:
                current.append("(")
                to_open -= 1
                dfs()
                to_open += 1
                current.pop()

            if n - to_open != 0:
                current.append(")")
                n -= 1
                dfs()
                n += 1
                current.pop()

        dfs()
        return result
