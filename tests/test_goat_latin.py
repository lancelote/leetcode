import pytest

from src.goat_latin import Solution


@pytest.mark.parametrize(
    "sentence,expected",
    (
        ("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"),
        (
            "The quick brown fox jumped over the lazy dog",
            "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa "
            "hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
        ),
    ),
)
def test_solution(sentence, expected):
    assert Solution().toGoatLatin(sentence) == expected
