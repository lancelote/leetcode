import random


class Solution:
    def __init__(self, nums: list[int]) -> None:
        self.original = nums
        self.current = nums.copy()

    def reset(self) -> list[int]:
        self.current = self.original.copy()
        return self.current

    def shuffle(self) -> list[int]:
        n = len(self.current)
        swap_idx = 0

        for _ in range(n):
            i = random.randint(swap_idx, n - 1)
            self.current[i], self.current[swap_idx] = (
                self.current[swap_idx],
                self.current[i],
            )
            swap_idx += 1

        return self.current
