class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        current_chars: set[str] = set()

        for x in s:
            while x in current_chars:
                current_chars.remove(s[left])
                left += 1
            current_chars.add(x)
            longest = max(longest, len(current_chars))

        return longest
