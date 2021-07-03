import pytest
from src.number_of_steps_to_reduce_a_number_to_zero import Solution


@pytest.mark.parametrize(
    "num,steps",
    [
        (14, 6),
        (8, 4),
        (123, 12),
    ],
)
def test_solution(num, steps):
    assert Solution().numberOfSteps(num) == steps
