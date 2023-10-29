class Solution:
    def poorPigs(self, buckets: int, min_to_die: int, min_to_test: int) -> int:
        count = 0

        while (min_to_test / min_to_die + 1) ** count < buckets:
            count += 1

        return count
