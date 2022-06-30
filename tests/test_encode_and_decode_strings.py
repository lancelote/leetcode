import pytest

from src.encode_and_decode_strings import Solution


@pytest.mark.parametrize(
    "text",
    [
        (["lint", "code", "love", "you"]),
        (["we", "say", ":", "yes"]),
    ],
)
def test_solution(text):
    solution = Solution()
    assert text == solution.decode(solution.encode(text))
