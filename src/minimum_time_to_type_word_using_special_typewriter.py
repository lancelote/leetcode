class Solution:
    def minTimeToType(self, word: str) -> int:
        pos = 0
        result = len(word)

        for char in word:
            new_pos = ord(char) - 97
            result += min(abs(new_pos - pos), 26 - abs(pos - new_pos))
            pos = new_pos

        return result
