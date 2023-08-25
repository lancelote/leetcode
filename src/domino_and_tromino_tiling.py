def get_state(t1: bool, t2: bool) -> int:
    state = 0
    if t1:
        state |= 1
    if t2:
        state |= 2
    return state


class Solution:
    def numTilings(self, n: int) -> int:
        dp = [[0] * 4 for _ in range(n + 1)]
        mod = 10**9 + 7

        def f(i: int, t1: bool, t2: bool) -> int:
            if i == n:
                return 1

            state = get_state(t1, t2)

            if dp[i][state]:
                return dp[i][state]

            t3 = t4 = i + 1 < n
            count = 0

            # t1 t3
            # t2 t4

            if t1 and t2 and t3:
                count += f(i + 1, False, True)
            if t1 and t2 and t4:
                count += f(i + 1, True, False)
            if t1 and not t2 and t3 and t4:
                count += f(i + 1, False, False)
            if not t1 and t2 and t3 and t4:
                count += f(i + 1, False, False)
            if t1 and t2:
                count += f(i + 1, True, True)
            if t1 and t2 and t3 and t4:
                count += f(i + 1, False, False)
            if t1 and not t2 and t3:
                count += f(i + 1, False, True)
            if not t1 and t2 and t4:
                count += f(i + 1, True, False)
            if not t1 and not t2:
                count += f(i + 1, True, True)

            dp[i][state] = count
            return dp[i][state]

        return f(0, True, True) % mod
