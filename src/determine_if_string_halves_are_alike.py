VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}


def count_vowels(text: str, start: int, stop: int) -> int:
    total_vowels = 0

    for i in range(start, stop):
        if text[i] in VOWELS:
            total_vowels += 1

    return total_vowels


class Solution:
    def halvesAreAlike(self, text: str) -> bool:
        middle = len(text) // 2
        first_half = count_vowels(text, start=0, stop=middle)
        second_half = count_vowels(text, start=middle, stop=len(text))
        return first_half == second_half
