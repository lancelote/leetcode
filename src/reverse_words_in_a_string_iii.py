from collections.abc import Iterator


def words(text: str) -> Iterator[str]:
    stack: list[str] = []

    for x in text.strip():
        if x == " ":
            yield "".join(stack)
            stack.clear()
        else:
            stack.append(x)

    yield "".join(stack)


class Solution:
    def reverseWords(self, s: str) -> str:
        result: list[str] = []

        for word in words(s):
            result.append(word[::-1])

        return " ".join(result)
