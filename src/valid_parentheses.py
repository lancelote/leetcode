TO_CLOSE: dict[str, str] = {
    "(": ")",
    "[": "]",
    "{": "}",
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []

        for x in s:
            if x in TO_CLOSE:
                stack.append(x)
            else:
                if not stack or TO_CLOSE[stack.pop()] != x:
                    return False

        return not stack
