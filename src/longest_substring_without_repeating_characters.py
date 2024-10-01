class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        left = 0

        for right, x in enumerate(s):
            while x in seen:
                seen.discard(s[left])
                left += 1

            seen.add(x)
            longest = max(longest, right - left + 1)

        return longest
