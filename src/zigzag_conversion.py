class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows <= 1:
            return s

        result = []

        first, second = num_rows * 2 - 2, 0

        start = 0
        while start < num_rows and start < len(s):
            i = start

            result.append(s[i])

            while True:
                i += first

                if first and i < len(s):
                    result.append(s[i])

                i += second

                if second and i < len(s):
                    result.append(s[i])

                if i >= len(s):
                    break

            start += 1
            first -= 2
            second += 2

        return "".join(result)
