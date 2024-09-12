from collections.abc import Iterator


def iter_words(s: str) -> Iterator[str]:
    buffer: list[str] = []

    for letter in s:
        if letter.isspace():
            if buffer:
                yield "".join(buffer)
                buffer.clear()
        else:
            buffer.append(letter)

    if buffer:
        yield "".join(buffer)


class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(iter_words(s))
        return " ".join(reversed(words))
