class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_length = max(len(a), len(b))
        result_bits = ["0"] * (max_length + 1)
        carry = 0

        for i in range(-1, -max_length - 2, -1):
            a_bit = int(a[i]) if abs(i) <= len(a) else 0
            b_bit = int(b[i]) if abs(i) <= len(b) else 0

            new_bit = a_bit + b_bit + carry
            carry = new_bit // 2
            result_bits[i] = str(new_bit % 2)

        result = "".join(result_bits)
        return "0" if result == "00" else result.lstrip("0")
