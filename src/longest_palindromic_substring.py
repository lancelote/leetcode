class Solution:
    def longestPalindrome(self, s: str) -> str:
        assert s

        longest = s[0]

        for i in range(len(s)):
            left, right = i - 1, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                longest = max(longest, s[left : right + 1], key=len)
                left -= 1
                right += 1

            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                longest = max(longest, s[left : right + 1], key=len)
                left -= 1
                right += 1

        return longest
