ROMAN: dict[str, int] = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, roman: str) -> int:
        assert roman

        last_int_value = ROMAN[roman[0]]
        result = 0

        for letter in roman:
            int_value = ROMAN[letter]

            if int_value > last_int_value:
                result += int_value - last_int_value * 2
            else:
                result += int_value

            last_int_value = int_value

        return result
