class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result: list[str] = []

        for i in range(1, n + 1):
            tmp = ""

            if i % 3 == 0:
                tmp = "Fizz"

            if i % 5 == 0:
                tmp += "Buzz"

            if not tmp:
                tmp = str(i)

            result.append(tmp)

        return result
