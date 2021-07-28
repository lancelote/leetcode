import pytest

from src.palindrome_number import Solution


@pytest.mark.parametrize(
    "x,expected", [(121, True), (-121, False), (10, False), (-101, False)]
)
def test_solution(x, expected):
    assert Solution().isPalindrome(x) == expected
