def count_words(sentence: str) -> int:
    return sentence.count(" ") + 1


class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max(count_words(x) for x in sentences)
