import pytest

from src.number_of_flowers_in_full_bloom import Solution


@pytest.mark.parametrize(
    "flowers,people,expected",
    (
        ([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11], [1, 2, 2, 2]),
        ([[1, 10], [3, 3]], [3, 3, 2], [2, 2, 1]),
        ([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11], [1, 2, 2, 2]),
    ),
)
def test_solution(flowers, people, expected):
    assert Solution().fullBloomFlowers(flowers, people) == expected
