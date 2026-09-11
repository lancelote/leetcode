def has_enough(available_counts: list[int], num: int) -> bool:
    num_count = [0] * 10

    for digit in map(int, str(num)):
        num_count[digit] += 1

    for has, need in zip(available_counts, num_count):
        if need > has:
            return False

    return True


class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        assert len(digits) >= 3

        result = 0
        counts = [0] * 10

        for digit in digits:
            counts[digit] += 1

        for num in range(100, 1000, 2):
            if has_enough(counts, num):
                result += 1

        return result
