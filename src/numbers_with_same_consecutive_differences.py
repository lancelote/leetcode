class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        result: list[int] = []

        def dfs(digit_n: int, current_num: int) -> None:
            if digit_n == 0:
                result.append(current_num)
                return

            last_digit = current_num % 10

            if last_digit - k >= 0:
                dfs(digit_n - 1, current_num * 10 + last_digit - k)
            if last_digit + k <= 9 and k != 0:
                dfs(digit_n - 1, current_num * 10 + last_digit + k)

        for i in range(1, 10):
            dfs(n - 1, i)
        return result
