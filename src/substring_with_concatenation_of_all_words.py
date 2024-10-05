class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        n = len(s)
        m = len(words[0])

        left = 0
        right = 0

        result = []

        words_bank: dict[str, int] = {}
        for word in words:
            words_bank[word] = words_bank.get(word, 0) + 1
        original_word_bank = words_bank.copy()

        while right < n - m + 1:
            right_substring = s[right : right + m]

            if right_substring in words_bank:
                words_bank[right_substring] -= 1
                if words_bank[right_substring] == 0:
                    del words_bank[right_substring]
                right += m
            else:
                left += 1
                right = left
                words_bank = original_word_bank.copy()

            if not words_bank:
                result.append(left)
                left += 1
                right = left
                words_bank = original_word_bank.copy()

        return result
