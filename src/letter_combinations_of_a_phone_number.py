DIGIT_TO_LETTERS = {
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
        if not digits:
            return []

        result: list[str] = []
        current: list[str] = []

        def dfs(i: int) -> None:
            if i == len(digits):
                result.append("".join(current))
                return

            digit = digits[i]
            for letter in DIGIT_TO_LETTERS[digit]:
                current.append(letter)
                dfs(i + 1)
                current.pop()

        dfs(0)
        return result
