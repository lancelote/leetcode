VOWELS = {"a", "e", "i", "o", "u"}


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result: list[str] = []

        for i, word in enumerate(sentence.split(), start=1):
            if word[0].lower() not in VOWELS:
                word = word[1:] + word[0]
            result.append(word + "ma" + "a" * i)

        return " ".join(result)
