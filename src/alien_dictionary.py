class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adj: dict[str, set[str]] = {}

        for word in words:
            for char in word:
                if char not in adj:
                    adj[char] = set()

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    adj[c1].add(c2)
                    break

        # False - visited
        # True - visited & in the current path
        visited: dict[str, bool] = {}
        result: list[str] = []

        def dfs(char: str) -> bool:
            if char in visited:
                return visited[char]

            visited[char] = True

            for child in adj[char]:
                if dfs(child):
                    return True

            visited[char] = False
            result.append(char)
            return False

        for char in adj:
            if dfs(char):
                return ""

        return "".join(result[::-1])
