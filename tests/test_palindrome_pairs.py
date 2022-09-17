import pytest

from src.palindrome_pairs import Solution


@pytest.mark.parametrize(
    "words,expected",
    [
        (
            ["abcd", "dcba", "lls", "s", "sssll"],
            [[1, 0], [0, 1], [3, 2], [2, 4]],
        ),
        (["bat", "tab", "cat"], [[1, 0], [0, 1]]),
        (["a", ""], [[0, 1], [1, 0]]),
    ],
)
def test_solution(words, expected):
    assert Solution().palindromePairs(words) == expected
