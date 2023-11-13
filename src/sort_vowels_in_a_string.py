VOWELS = {"a", "e", "i", "o", "u"}


class Solution:
    def sortVowels(self, s: str) -> str:
        result = list(s)

        vowels = sorted(x for x in s if x.lower() in VOWELS)

        i = 0
        for vowel in vowels:
            while s[i].lower() not in VOWELS:
                i += 1
            result[i] = vowel
            i += 1

        return "".join(result)
