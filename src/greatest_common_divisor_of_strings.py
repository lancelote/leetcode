def is_divisor(length: int, str1: str, str2: str) -> bool:
    if len(str1) % length or len(str2) % length:
        return False

    factor1 = len(str1) // length
    factor2 = len(str2) // length

    return str1[:length] * factor1 == str1 and str1[:length] * factor2 == str2


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        assert str1
        assert str2

        for length in range(min(len(str1), len(str2)), 0, -1):
            if is_divisor(length, str1, str2):
                return str1[:length]

        return ""
