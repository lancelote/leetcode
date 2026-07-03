VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}


class Solution:
    def reverseVowels(self, s: str) -> str:
        result: list[str] = []

        vowels: list[str] = []
        for x in s:
            if x in VOWELS:
                vowels.append(x)

        for x in s:
            if x in VOWELS:
                result.append(vowels.pop())
            else:
                result.append(x)

        return "".join(result)
