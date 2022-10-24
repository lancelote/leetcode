class Solution:
    def maxLength(self, arr: list[str]) -> int:
        char_set: set[str] = set()

        def overlap(s: str) -> bool:
            prev: set[str] = set()

            for char in s:
                if char in char_set or char in prev:
                    return True
                prev.add(char)
            return False

        def backtrack(i: int) -> int:
            if i == len(arr):
                return len(char_set)

            result = 0

            if not overlap(arr[i]):
                char_set.update(arr[i])
                result = backtrack(i + 1)
                char_set.difference_update(arr[i])

            return max(result, backtrack(i + 1))

        return backtrack(0)
