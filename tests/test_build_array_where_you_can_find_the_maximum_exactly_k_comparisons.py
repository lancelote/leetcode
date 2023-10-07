import pytest

from src.build_array_where_you_can_find_the_maximum_exactly_k_comparisons import (  # noqa
    Solution,
)


@pytest.mark.parametrize(
    "n,m,k,expected",
    (
        (2, 3, 1, 6),
        (5, 2, 3, 0),
        (9, 1, 1, 1),
    ),
)
def test_solution(n, m, k, expected):
    assert Solution().numOfArrays(n, m, k) == expected
