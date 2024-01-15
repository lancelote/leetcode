LETTERS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        n = len(digits)
        result: list[str] = []

        def dfs(i: int, so_far: list[str]) -> None:
            if i == n:
                result.append("".join(so_far))
                return

            digit = digits[i]

            for x in LETTERS[digit]:
                so_far.append(x)
                dfs(i + 1, so_far)
                so_far.pop()

        if digits:
            dfs(0, [])

        return result
