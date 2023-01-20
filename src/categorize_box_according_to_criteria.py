class Solution:
    def categorizeBox(
        self, length: int, width: int, height: int, mass: int
    ) -> str:
        volume = length * width * height
        if (
            length >= 10_000
            or width >= 10_000
            or height >= 10_000
            or volume >= 10**9
        ):
            if mass >= 100:
                return "Both"
            else:
                return "Bulky"
        elif mass >= 100:
            return "Heavy"
        else:
            return "Neither"
