import pytest

from src.subtract_the_product_and_sum_of_digits_of_an_integer import Solution


@pytest.mark.parametrize(
    """number,expected_difference""",
    [
        (234, 15),
        (4421, 21),
    ],
)
def test_solution(number, expected_difference):
    assert Solution().subtractProductAndSum(number) == expected_difference
