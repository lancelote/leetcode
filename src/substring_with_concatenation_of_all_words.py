class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        n = len(s)
        m = len(words[0])
        substring_length = m * len(words)

        result: list[int] = []
        words_bank: dict[str, int] = {}

        for word in words:
            words_bank[word] = words_bank.get(word, 0) + 1

        def dfs(start: int = 0) -> bool:
            if not words_bank:
                return True

            substring = s[start : start + m]

            if substring in words_bank:
                words_bank[substring] -= 1
                if words_bank[substring] == 0:
                    del words_bank[substring]

                success = dfs(start + m)

                words_bank[substring] = words_bank.get(substring, 0) + 1
                return success

            return False

        for i in range(n - substring_length + 1):
            if dfs(i):
                result.append(i)

        return result
