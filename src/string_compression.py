class Solution:
    def compress(self, chars: list[str]) -> int:
        assert chars

        i = 0
        count = 0
        prev = chars[0]

        def write(x: str, n: int) -> None:
            nonlocal i
            assert n

            chars[i] = x
            i += 1

            if n != 1:
                for digit in str(n):
                    chars[i] = digit
                    i += 1

        for char in chars:
            if char == prev:
                count += 1
            else:
                write(prev, count)
                count = 1
            prev = char

        write(prev, count)
        return i
