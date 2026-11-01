class Solution:
    def reverse_part(self, start: int, end: int, s: list[str]) -> None:
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverse_whole(self, s: list[str]) -> None:
        self.reverse_part(0, len(s) - 1, s)

    def reverseWords(self, s: list[str]) -> None:
        self.reverse_whole(s)

        word_start = 0

        char = ""
        for idx, char in enumerate(s):
            if char == " ":
                self.reverse_part(word_start, idx - 1, s)
                word_start = idx + 1

        if char != " ":
            self.reverse_part(word_start, len(s) - 1, s)
