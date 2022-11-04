from collections import Counter


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        answer = 0
        counter = Counter(words)

        for word in words:
            reversed_word = word[::-1]

            if word == reversed_word and counter[word] >= 2:
                counter[word] -= 2
                answer += 4
            elif (
                word != reversed_word
                and counter[word] >= 1
                and counter[reversed_word] >= 1
            ):
                counter[word] -= 1
                counter[reversed_word] -= 1
                answer += 4

        for word, count in counter.items():
            if count > 0 and word[0] == word[1]:
                answer += 2
                break

        return answer
