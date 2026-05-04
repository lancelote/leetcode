import random

from src.shuffle_an_array import Solution


def test_solution():
    s = Solution([1, 2, 3])

    random.seed(42)

    assert s.shuffle() == [3, 2, 1]
    assert s.reset() == [1, 2, 3]
    assert s.shuffle() == [3, 1, 2]
