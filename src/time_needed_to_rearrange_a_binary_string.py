class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        num_of_zeros = 0
        pairs_of_ones = 0

        try:
            last_one_idx = s.rindex("1")
        except ValueError:
            return 0

        for i in range(last_one_idx):
            if s[i] == "0":
                num_of_zeros += 1

                if s[i + 1] == "0":
                    # possible pair of ones is too far away to consider
                    pairs_of_ones = max(0, pairs_of_ones - 1)

            if s[i] == "1" and s[i + 1] == "1" and num_of_zeros:
                pairs_of_ones += 1

        return num_of_zeros + pairs_of_ones
