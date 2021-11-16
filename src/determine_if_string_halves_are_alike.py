VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}


def count_vowels(text: str, start: int, stop: int) -> int:
    total_vowels = 0

    for i in range(start, stop):
        if text[i] in VOWELS:
            total_vowels += 1

    return total_vowels


class Solution:
    def halvesAreAlike(self, text: str) -> bool:
        first_half = count_vowels(text, 0, len(text) // 2)
        second_half = count_vowels(text, len(text) // 2, len(text))
        return first_half == second_half
