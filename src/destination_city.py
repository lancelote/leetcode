class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        from_cities = {x for [x, _] in paths}
        to_cities = {x for [_, x] in paths}
        [destination] = to_cities - from_cities
        return destination
