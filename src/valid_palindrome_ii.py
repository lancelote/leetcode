class Solution:
    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.is_palindrome(
                    s, left + 1, right
                ) or self.is_palindrome(s, left, right - 1)

            left += 1
            right -= 1

        return True
