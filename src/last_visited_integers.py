class Solution:
    def lastVisitedIntegers(self, words: list[str]) -> list[int]:
        result: list[int] = []
        stack: list[int] = []
        shift = 0

        for i, word in enumerate(words):
            if word == "prev":
                shift += 1

                if len(stack) - shift >= 0:
                    result.append(stack[-shift])
                else:
                    result.append(-1)
            else:
                shift = 0
                stack.append(int(word))

        return result
