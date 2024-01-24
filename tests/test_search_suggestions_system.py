import pytest

from src.search_suggestions_system import Solution


@pytest.mark.parametrize(
    "products,search_word,expected",
    (
        (
            ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
            "mouse",
            [
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
        ),
        (
            ["havana"],
            "havana",
            [
                ["havana"],
                ["havana"],
                ["havana"],
                ["havana"],
                ["havana"],
                ["havana"],
            ],
        ),
        (
            ["havana"],
            "tatiana",
            [[], [], [], [], [], [], []],
        ),
    ),
)
def test_solution(products, search_word, expected):
    assert Solution().suggestedProducts(products, search_word) == expected
