class Solution:
    def carFleet(
        self, target: int, positions: list[int], speeds: list[int]
    ) -> int:
        assert positions
        assert speeds

        cars = sorted(zip(positions, speeds), reverse=True)
        stack: list[float] = []

        for car_pos, car_speed in cars:
            assert car_speed > 0
            car_time = (target - car_pos) / car_speed

            if not stack or car_time > stack[-1]:
                stack.append(car_time)

        return len(stack)
