VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}


class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        result = list(s)

        left = 0
        right = n - 1

        while left < right:
            if s[left] not in VOWELS:
                left += 1
                continue

            if s[right] not in VOWELS:
                right -= 1
                continue

            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1

        return "".join(result)
