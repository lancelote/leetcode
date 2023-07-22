VOWELS = {"a", "e", "i", "o", "u"}


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels: list[str] = []

        for x in s:
            if x.lower() in VOWELS:
                vowels.append(x)

        vowels.sort(reverse=True)
        result: list[str] = []

        for x in s:
            if x.lower() in VOWELS:
                result.append(vowels.pop())
            else:
                result.append(x)

        return "".join(result)
