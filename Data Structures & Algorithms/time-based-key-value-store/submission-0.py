class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values_list = self.map[key]

        if not self.map[key] or timestamp < values_list[0][1]:
            return ""

        if timestamp >= values_list[-1][1]:
            return values_list[-1][0]

        low = 0
        high = len(values_list) - 1
        while low <= high:
            mid = (low + high) // 2

            val_prev, timestamp_prev = values_list[mid]
            if timestamp_prev == timestamp:
                return val_prev
            elif timestamp_prev > timestamp:
                high = mid - 1
            else:
                low = mid + 1

        return values_list[high][0]
