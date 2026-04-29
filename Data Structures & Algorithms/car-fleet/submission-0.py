class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet_count = 0

        cars = list(zip(position, speed))
        cars.sort(key=lambda c: c[0], reverse=True)
        prev_time = -1
        for curr_position, curr_speed in cars:
            arrival_time = (target - curr_position) / float(curr_speed)
            if arrival_time > prev_time:
                car_fleet_count += 1
                prev_time = arrival_time

        return car_fleet_count