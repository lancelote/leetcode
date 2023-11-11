MOD = 10**9 + 7


class Solution:
    def countHomogenous(self, s: str) -> int:
        result = 0
        prev = ""
        curr_stack = 1

        for x in s:
            if x == prev:
                curr_stack += 1
            else:
                curr_stack = 1

            result += curr_stack
            prev = x

        return result % MOD
