from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_count = Counter(str(n))

        for i in range(30):
            power_of_2 = 1 << i
            if n_count == Counter(str(power_of_2)):
                return True

        return False
