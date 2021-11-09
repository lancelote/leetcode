class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            ch_index = word.index(ch)
            to_reverse = word[: ch_index + 1]
            to_leave = word[ch_index + 1 :]
            return to_reverse[::-1] + to_leave
        except ValueError:
            return word
