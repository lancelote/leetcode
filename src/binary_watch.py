class Solution:
    def readBinaryWatch(self, turned_on: int) -> list[str]:
        result: list[str] = []

        for hour in range(12):
            for minute in range(60):
                if hour.bit_count() + minute.bit_count() == turned_on:
                    result.append(f"{hour}:{minute:02}")

        return result
