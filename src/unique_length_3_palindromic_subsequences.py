from collections import Counter
from string import ascii_lowercase


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result: set[tuple[str, str]] = set()
        left: set[str] = set()
        right: dict[str, int] = Counter(s)

        for i in range(len(s) - 1):
            right[s[i]] -= 1
            for x in ascii_lowercase:
                if x in left and x in right and right[x]:
                    result.add((s[i], x))
            left.add(s[i])
        return len(result)
