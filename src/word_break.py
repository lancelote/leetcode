class Solution:
    def wordBreak(self, s: str, word_dict: list[str]) -> bool:
        n = len(s)
        cache: dict[int, bool] = {}

        def dfs(i: int) -> bool:
            if i == n:
                return True

            if i > n:
                return False

            if i in cache:
                return cache[i]

            for word in word_dict:
                if s[i : i + len(word)] == word:
                    result = dfs(i + len(word))
                    cache[i + len(word)] = result
                    if result:
                        return True

            return False

        return dfs(0)
