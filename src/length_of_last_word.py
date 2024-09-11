class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i].isalpha():
                length += 1
            elif length:
                break

        return length
