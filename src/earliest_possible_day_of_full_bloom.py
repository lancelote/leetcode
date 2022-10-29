class Solution:
    def earliestFullBloom(
        self, plant_time: list[int], grow_time: list[int]
    ) -> int:
        plants = [(x, y) for x, y in zip(grow_time, plant_time)]
        plants.sort(reverse=True)

        current_day = 0
        last_day = 0

        for grow, plant in plants:
            current_day += plant
            last_day = max(last_day, current_day + grow)

        return last_day
