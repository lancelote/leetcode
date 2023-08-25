import pytest

from src.domino_and_tromino_tiling import Solution


@pytest.mark.parametrize(
    "n,expected",
    (
        (3, 5),
        (1, 1),
    ),
)
def test_solution(n, expected):
    assert Solution().numTilings(n) == expected
