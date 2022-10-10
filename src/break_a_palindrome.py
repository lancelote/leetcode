class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i, char in enumerate(palindrome):
            if char != "a":
                return palindrome[:i] + "a" + palindrome[i + 1 :]
        return palindrome[-1] + "b" if palindrome[:-1] else ""
