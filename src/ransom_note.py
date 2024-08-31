from collections import Counter


class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        available = Counter(magazine)

        for letter in ransom_note:
            if available[letter] == 0:
                return False
            available[letter] -= 1

        return True
