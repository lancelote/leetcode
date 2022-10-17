class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        n = 0

        for char in sentence:
            shift = ord(char) - 97
            n |= 1 << shift

        return n == 67108863
