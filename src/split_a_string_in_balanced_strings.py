class Solution:
    def balancedStringSplit(self, line: str) -> int:
        balanced_cuts = rs = ls = 0

        for letter in line:
            if letter == "R":
                rs += 1
            elif letter == "L":
                ls += 1

            if rs == ls:
                balanced_cuts += 1

        return balanced_cuts
