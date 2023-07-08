class Solution:
    def relocateMarbles(
        self, nums: list[int], move_from: list[int], move_to: list[int]
    ) -> list[int]:
        positions = set(nums)

        for from_pos, to_pos in zip(move_from, move_to):
            positions.remove(from_pos)
            positions.add(to_pos)

        return sorted(list(positions))
