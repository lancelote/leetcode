import pytest

from src.decode_xored_array import Solution


@pytest.mark.parametrize(
    "encoded,first,decoded",
    [
        ([1, 2, 3], 1, [1, 0, 2, 1]),
        ([6, 2, 7, 3], 4, [4, 2, 0, 7, 4]),
    ],
)
def test_solution(encoded, first, decoded):
    assert Solution().decode(encoded, first) == decoded
