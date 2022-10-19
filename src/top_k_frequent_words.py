class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counter: dict[str, int] = {}

        for word in words:
            counter[word] = counter.get(word, 0) + 1

        result = []

        for word, _ in sorted(counter.items(), key=lambda x: (-x[1], x[0])):
            if k == 0:
                break

            result.append(word)
            k -= 1

        return result
