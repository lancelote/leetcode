class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        weak_count = 0
        max_so_far = 0
        sorted_props = sorted(properties, key=lambda x: (-x[0], x[1]))

        for _, defense in sorted_props:
            if defense < max_so_far:
                weak_count += 1
            else:
                max_so_far = defense

        return weak_count
