import pytest

from src.minimum_time_to_type_word_using_special_typewriter import Solution


@pytest.mark.parametrize(
    "word,seconds",
    [
        ("abc", 5),
        ("bza", 7),
        ("zjpc", 34),
    ],
)
def test_solution(word, seconds):
    assert Solution().minTimeToType(word) == seconds
