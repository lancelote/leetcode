from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack: list[str] = []
        on_stack: set[str] = set()

        for x in s:
            while (
                stack
                and stack[-1] >= x
                and count[stack[-1]] != 0
                and x not in on_stack
            ):
                on_stack.remove(stack.pop())
            if x not in on_stack:
                stack.append(x)
                on_stack.add(x)
            count[x] -= 1

        return "".join(stack)
