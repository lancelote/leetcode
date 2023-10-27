class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_sub = ""
        longest_len = 0

        def check_palindrome(left: int, right: int) -> None:
            nonlocal longest_sub
            nonlocal longest_len

            current = 0

            while left >= 0 and right < n:
                if s[left] == s[right]:
                    current += 1 + (left != right)
                else:
                    break

                if current > longest_len:
                    longest_len = current
                    longest_sub = s[left : right + 1]

                left -= 1
                right += 1

        for i in range(n):
            check_palindrome(i, i)
            check_palindrome(i, i + 1)

        return longest_sub
