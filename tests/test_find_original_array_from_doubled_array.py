import pytest

from src.find_original_array_from_doubled_array import Solution


@pytest.mark.parametrize(
    "changed,expected_original",
    [
        ([1, 3, 4, 2, 6, 8], [1, 3, 4]),
        ([6, 3, 0, 1], []),
        ([1], []),
        ([0], []),
    ],
)
def test_solution(changed, expected_original):
    assert Solution().findOriginalArray(changed) == expected_original
