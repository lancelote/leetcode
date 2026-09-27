class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        if letters[-1] <= target:
            return letters[0]

        while left < right:
            middle = left + (right - left) // 2
            guess = letters[middle]

            if guess <= target:
                left = middle + 1
            else:
                right = middle

        return letters[right]
