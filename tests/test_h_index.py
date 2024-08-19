import pytest

from src.h_index import Solution


@pytest.mark.parametrize(
    "expected,citations",
    (
        (3, [3, 0, 6, 1, 5]),
        (1, [1, 3, 1]),
    ),
)
def test_solution(expected, citations):
    assert expected == Solution().hIndex(citations)
