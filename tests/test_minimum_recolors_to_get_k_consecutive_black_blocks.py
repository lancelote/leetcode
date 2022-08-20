import pytest

from src.minimum_recolors_to_get_k_consecutive_black_blocks import Solution


@pytest.mark.parametrize(
    "blocks,k,expected",
    [
        ("WBBWWBBWBW", 7, 3),
        ("WBWBBBW", 2, 0),
    ],
)
def test_solution(blocks, k, expected):
    assert Solution().minimumRecolors(blocks, k) == expected
