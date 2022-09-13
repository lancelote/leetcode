class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        n_bytes = 0

        for num in data:
            mask = 128

            if n_bytes == 0:
                while mask & num:
                    n_bytes += 1
                    mask = mask >> 1

                if n_bytes == 0:
                    continue

                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                if num ^ 64 < 192:
                    return False
            n_bytes -= 1
        return n_bytes == 0
