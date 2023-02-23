class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores: list[int] = []

        for op in operations:
            match op:
                case "+":
                    scores.append(scores[-1] + scores[-2])
                case "D":
                    scores.append(scores[-1] * 2)
                case "C":
                    scores.pop()
                case _:
                    scores.append(int(op))

        return sum(scores)
