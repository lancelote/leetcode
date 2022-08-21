import pytest

from src.stamping_the_sequence import Solution


@pytest.mark.parametrize(
    "stamp,target,result",
    [
        ("abc", "ababc", [0, 2]),
        ("abca", "aabcaca", [3, 0, 1]),
        ("aye", "eyeye", []),
        ("mda", "mdadddaaaa", []),
    ],
)
def test_solution(stamp, target, result):
    assert Solution().movesToStamp(stamp, target) == result
