import pytest

from src.build_an_array_with_stack_operations import Solution


@pytest.mark.parametrize(
    "target,n,expected",
    (
        ([1, 3], 3, ["Push", "Push", "Pop", "Push"]),
        ([1, 2, 3], 3, ["Push", "Push", "Push"]),
        ([1, 2], 4, ["Push", "Push"]),
    ),
)
def test_solution(target, n, expected):
    assert Solution().buildArray(target, n) == expected
