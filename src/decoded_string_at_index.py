class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        lens = [0]
        n = len(s)

        for x in s:
            if x.isalpha():
                lens.append(lens[-1] + 1)
            else:
                lens.append(lens[-1] * int(x))

        for i in range(n, 0, -1):
            k %= lens[i]
            if k == 0 and s[i - 1].isalpha():
                return s[i - 1]

        raise ValueError
