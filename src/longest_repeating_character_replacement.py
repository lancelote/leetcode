from collections import defaultdict
from typing import DefaultDict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts: DefaultDict[str, int] = defaultdict(int)
        longest = 0
        max_f = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            max_f = max(max_f, counts[s[right]])

            while (right - left + 1) - max_f > k:
                counts[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
