VOWELS = {"a", "e", "i", "o", "u"}


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0

        for i in range(k):
            if s[i] in VOWELS:
                count += 1

        max_count = count

        for i in range(k, len(s)):
            if s[i - k] in VOWELS:
                count -= 1
            if s[i] in VOWELS:
                count += 1
            max_count = max(count, max_count)

        return max_count
