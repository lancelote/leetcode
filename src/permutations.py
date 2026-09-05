import copy


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations: list[list[int]] = [[]]

        for num in nums:
            new_permutations: list[list[int]] = []

            for permutation in permutations:
                for i in range(len(permutation) + 1):
                    permutation_copy = copy.copy(permutation)
                    permutation_copy.insert(i, num)
                    new_permutations.append(permutation_copy)

            permutations = new_permutations

        return permutations
