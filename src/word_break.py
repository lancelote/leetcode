class Solution:
    def wordBreak(self, s: str, word_dict: list[str]) -> bool:
        cache: dict[int, bool] = {}

        def dp(idx: int) -> bool:
            if idx < 0:
                return True

            if idx in cache:
                return cache[idx]

            for word in word_dict:
                if s[idx - len(word) + 1 : idx + 1] == word and dp(
                    idx - len(word)
                ):
                    cache[idx] = True
                    return True

            cache[idx] = False
            return False

        return dp(len(s) - 1)
