import pytest

from src.numbers_with_same_consecutive_differences import Solution


@pytest.mark.parametrize(
    "n,k,expected",
    [
        (3, 7, [181, 292, 707, 818, 929]),
        (
            2,
            1,
            [
                10,
                12,
                21,
                23,
                32,
                34,
                43,
                45,
                54,
                56,
                65,
                67,
                76,
                78,
                87,
                89,
                98,
            ],
        ),
        (2, 0, [11, 22, 33, 44, 55, 66, 77, 88, 99]),
    ],
)
def test_solution(n, k, expected):
    assert Solution().numsSameConsecDiff(n, k) == expected
