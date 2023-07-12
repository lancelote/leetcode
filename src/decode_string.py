from collections.abc import Iterator


def tokens(s: str) -> Iterator[int | str]:
    i = 0

    while i < len(s):
        current: list[str] = []

        if s[i].isnumeric():
            while i < len(s) and s[i].isnumeric():
                current.append(s[i])
                i += 1
            yield int("".join(current))
        elif s[i].isalpha():
            while i < len(s) and s[i].isalpha():
                current.append(s[i])
                i += 1
            yield "".join(current)
        else:
            yield s[i]
            i += 1


class Solution:
    def decodeString(self, s: str) -> str:
        stack: list[int | str] = []

        for x in tokens(s):
            if x == "]":
                while isinstance(stack[-2], str):
                    a, b = stack.pop(), stack.pop()
                    stack.append(b + a)  # type: ignore

                a, b = stack.pop(), stack.pop()
                stack.append(b * a)  # type: ignore
            elif x == "[":
                continue
            else:
                stack.append(x)

        return "".join(stack)  # type: ignore
