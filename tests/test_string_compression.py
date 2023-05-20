import pytest

from src.string_compression import Solution


@pytest.mark.parametrize(
    "chars,expected_n,expected_arr",
    (
        (
            ["a", "a", "b", "b", "c", "c", "c"],
            6,
            ["a", "2", "b", "2", "c", "3"],
        ),
        (
            ["a"],
            1,
            ["a"],
        ),
        (
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
            4,
            ["a", "b", "1", "2"],
        ),
    ),
)
def test_solution(chars, expected_n, expected_arr):
    assert Solution().compress(chars) == expected_n
    assert chars[:expected_n] == expected_arr
