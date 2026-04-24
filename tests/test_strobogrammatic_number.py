import pytest

from src.strobogrammatic_number import Solution


@pytest.mark.parametrize(
    "num,expected",
    (
        ("69", True),
        ("88", True),
        ("962", False),
        ("1", True),
    ),
)
def test_solution(num, expected):
    assert Solution().isStrobogrammatic(num) is expected
