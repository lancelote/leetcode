class Solution:
    def countTime(self, time: str) -> int:
        hour, minute = time.split(":")

        count = 1

        if minute[0] == "?":
            count *= 6

        if minute[1] == "?":
            count *= 10

        if hour == "??":
            count *= 24
        elif hour[0] == "?" and int(hour[1]) < 4:
            count *= 3
        elif hour[0] == "?":
            count *= 2
        elif hour[1] == "?" and int(hour[0]) == 2:
            count *= 4
        elif hour[1] == "?":
            count *= 10

        return count
