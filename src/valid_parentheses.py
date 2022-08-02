TO_CLOSING = {"(": ")", "{": "}", "[": "]"}


class Solution:
    def isValid(self, s: str) -> bool:
        expected_stack: list[str] = []
        for paren in s:
            if paren in TO_CLOSING:
                expected_stack.append(TO_CLOSING[paren])
            elif not expected_stack or expected_stack.pop() != paren:
                return False
        return not expected_stack
