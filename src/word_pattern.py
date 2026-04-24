class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        ch_to_word: dict[str, str] = {}
        seen_words: set[str] = set()

        for i in range(len(words)):
            ch = pattern[i]
            word = words[i]

            if ch in ch_to_word and ch_to_word[ch] != word:
                return False

            if ch not in ch_to_word and word in seen_words:
                return False

            ch_to_word[ch] = word
            seen_words.add(word)

        return True
