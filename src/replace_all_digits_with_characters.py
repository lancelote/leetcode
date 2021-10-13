class Solution:
    def shift(self, letter: str, index: int) -> str:
        return chr(ord(letter) + index)

    def replaceDigits(self, s: str) -> str:
        result = []

        for i, letter in enumerate(s):
            if letter.isdigit():
                result.append(self.shift(s[i - 1], int(letter)))
            else:
                result.append(letter)

        return "".join(result)
