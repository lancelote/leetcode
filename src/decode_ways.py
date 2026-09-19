class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache: list[int] = [0] * (n + 1)
        cache[n] = 1

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                cache[i] = 0
            else:
                cache[i] = cache[i + 1]

                if i < (n - 1) and int(s[i : i + 2]) <= 26:
                    cache[i] += cache[i + 2]

        return cache[0]
