MODULO = 10**9 + 7.0


class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        result = []

        for left, right in queries:
            count = 0
            powers_of_2 = 0

            for i in range(32):
                mask = 1 << i

                if n & mask:
                    count += 1
                else:
                    continue

                if count > right + 1:
                    break

                if count >= left + 1:
                    powers_of_2 += i

            result.append(int(2**powers_of_2 % MODULO))

        return result
