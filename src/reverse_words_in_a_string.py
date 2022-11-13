class Solution:
    def reverseWords(self, s: str) -> str:
        result = s.split()
        return " ".join(result[::-1])
