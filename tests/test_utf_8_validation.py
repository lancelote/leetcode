import pytest

from src.utf_8_validation import Solution


@pytest.mark.parametrize(
    "data,expected",
    [
        ([197, 130, 1], True),
        ([235, 140, 4], False),
        ([255], False),
        ([145], False),
        ([240, 162, 138, 147, 145], False),
        ([237], False),
        ([228, 189, 160, 229, 165, 189, 13, 10], True),
    ],
)
def test_solution(data, expected):
    assert Solution().validUtf8(data) is expected
