class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window: set[str] = set()
        left = 0
        longest = 0

        for x in s:
            while x in window:
                window.remove(s[left])
                left += 1
            window.add(x)
            longest = max(longest, len(window))

        return longest
