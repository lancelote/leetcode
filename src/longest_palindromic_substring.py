class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = [0, 0]

        def expand_palindrome(left: int, right: int) -> None:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > result[1] - result[0]:
                    result[0] = left
                    result[1] = right
                left -= 1
                right += 1

        for i in range(len(s)):
            expand_palindrome(i, i)
            expand_palindrome(i, i + 1)

        start, end = result
        return s[start : end + 1]
