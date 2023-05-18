class Solution:
    def reverseWords(self, s: str) -> str:
        result: list[str] = []

        word: list[str] = []

        for char in s:
            if char == " " and word:
                result.append("".join(word))
                word = []
            elif char != " ":
                word.append(char)

        if word:
            result.append("".join(word))

        left = 0
        right = len(result) - 1

        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1

        return " ".join(result)
