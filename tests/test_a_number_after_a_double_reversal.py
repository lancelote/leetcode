import pytest

from src.a_number_after_a_double_reversal import Solution


@pytest.mark.parametrize(
    "num,equal",
    [
        (526, True),
        (1800, False),
        (0, True),
    ],
)
def test_solution(num, equal):
    assert Solution().isSameAfterReversals(num) == equal
