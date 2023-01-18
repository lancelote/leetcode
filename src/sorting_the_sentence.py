from collections.abc import Iterator


def tuples(sentence: str) -> Iterator[tuple[int, str]]:
    for item in sentence.split(" "):
        yield int(item[-1]), item[:-1]


class Solution:
    def sortSentence(self, sentence: str) -> str:
        return " ".join(t[1] for t in sorted(tuples(sentence)))
