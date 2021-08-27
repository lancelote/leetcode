class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)

        def is_consistent(word: str) -> bool:
            return all(x in allowed_set for x in word)

        return sum(is_consistent(word) for word in words)
