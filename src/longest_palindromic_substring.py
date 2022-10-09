class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = ""
        longest = 0

        def find_longest(left: int, right: int) -> None:
            nonlocal longest
            nonlocal result

            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > longest:
                    result = s[left : right + 1]
                    longest = right - left + 1
                left -= 1
                right += 1

        for i in range(n):
            find_longest(i, i)
            find_longest(i, i + 1)

        return result
