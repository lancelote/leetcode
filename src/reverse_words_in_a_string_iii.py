class Solution:
    def reverseWord(self, word: str) -> str:
        result = list(word)
        left, right = 0, len(word) - 1

        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1

        return "".join(result)

    def reverseWords(self, s: str) -> str:
        return " ".join(self.reverseWord(word) for word in s.split(" "))
