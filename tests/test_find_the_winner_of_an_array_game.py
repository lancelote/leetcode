import pytest

from src.find_the_winner_of_an_array_game import Solution


@pytest.mark.parametrize(
    "arr,k,expected",
    (
        ([2, 1, 3, 5, 4, 6, 7], 2, 5),
        ([3, 2, 1], 10, 3),
        ([1, 11, 22, 33, 44, 55, 66, 77, 88, 99], 1_000_000_000, 99),
    ),
)
def test_solution(arr, k, expected):
    assert Solution().getWinner(arr, k) == expected
