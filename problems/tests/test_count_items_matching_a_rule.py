import pytest
from src.count_items_matching_a_rule import Solution


@pytest.mark.parametrize(
    "items,rule_key,rule_value,matching",
    [
        (
            [
                ["phone", "blue", "pixel"],
                ["computer", "silver", "lenovo"],
                ["phone", "gold", "iphone"],
            ],
            "color",
            "silver",
            1,
        ),
        (
            [
                ["phone", "blue", "pixel"],
                ["computer", "silver", "phone"],
                ["phone", "gold", "iphone"],
            ],
            "type",
            "phone",
            2,
        ),
    ],
)
def test_solution(items, rule_key, rule_value, matching):
    assert Solution().countMatches(items, rule_key, rule_value) == matching
