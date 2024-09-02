class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        letter_to_word: dict[str, str] = {}
        word_to_letter: dict[str, str] = {}

        for letter, word in zip(pattern, s.split()):
            if letter_to_word.get(letter, word) != word:
                return False
            if word_to_letter.get(word, letter) != letter:
                return False

            letter_to_word[letter] = word
            word_to_letter[word] = letter

        return True
