class Solution:
    def countAndSay(self, n: int) -> str:
        result: list[str] = ["1"]

        for _ in range(n - 1):
            new_result: list[str] = []

            count = 0
            prev = result[0]

            for char in result:
                if prev == char:
                    count += 1
                else:
                    new_result.append(str(count))
                    new_result.append(prev)

                    count = 1
                    prev = char

            new_result.append(str(count))
            new_result.append(result[-1])

            result = new_result

        return "".join(result)
