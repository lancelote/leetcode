import pytest

from src.find_the_original_array_of_prefix_xor import Solution


@pytest.mark.parametrize(
    "pref,expected",
    (
        ([5, 2, 0, 3, 1], [5, 7, 2, 3, 2]),
        ([13], [13]),
    ),
)
def test_solution(pref, expected):
    assert Solution().findArray(pref) == expected
