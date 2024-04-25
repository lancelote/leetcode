def read4(_: list[str]) -> int:
    raise NotImplementedError


class Solution:
    def read(self, buf: list[str], n: int) -> int:
        pointer = 0
        buf4 = [""] * 4

        while n and (last_read := read4(buf4)) > 0:
            for i in range(min(n, last_read)):
                buf[pointer] = buf4[i]
                pointer += 1

            n = max(0, n - last_read)

        return pointer
