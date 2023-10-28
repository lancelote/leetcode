MOD = 10**9 + 7
VOWELS = {"a", "e", "i", "o", "u"}


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        cache: dict[tuple[str, int], int] = {}

        def dfs(last: str, i: int) -> int:
            if i == n:
                return 1

            if (last, i) in cache:
                return cache[(last, i)]

            if last == "a":
                result = dfs("e", i + 1)
            elif last == "e":
                result = dfs("a", i + 1) + dfs("i", i + 1)
            elif last == "i":
                result = sum(dfs(x, i + 1) for x in VOWELS - {"i"})
            elif last == "o":
                result = dfs("i", i + 1) + dfs("u", i + 1)
            elif last == "u":
                result = dfs("a", i + 1)
            else:
                raise ValueError

            cache[(last, i)] = result
            return result

        return sum(dfs(x, 1) for x in VOWELS) % MOD
