class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        char_to_idx = {x: i for i, x in enumerate(order)}

        def is_good_order(word1: str, word2: str) -> bool:
            for i, x1 in enumerate(word1):
                if i >= len(word2):
                    return False

                x2 = word2[i]

                i1 = char_to_idx[x1]
                i2 = char_to_idx[x2]

                if i1 > i2:
                    return False
                elif i1 == i2:
                    continue
                else:
                    return True

            return True

        for i in range(len(words) - 1):
            if not is_good_order(words[i], words[i + 1]):
                return False

        return True
