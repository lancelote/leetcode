class Solution:
    def countMatches(
        self, items: list[list[str]], rule_key: str, rule_value: str
    ) -> int:
        count = 0

        for item_type, item_color, item_name in items:
            if rule_key == "type" and item_type == rule_value:
                count += 1
            elif rule_key == "color" and item_color == rule_value:
                count += 1
            elif rule_key == "name" and item_name == rule_value:
                count += 1

        return count
