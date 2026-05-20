from bisect import bisect_left
class TimeMap:

    def __init__(self):
        self.store: dict[str, List[tuple[int, str]]] = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]

        timestamps = [value[0] for value in values]

        index = bisect_left(timestamps, timestamp)

        if index < len(timestamps) and timestamps[index] == timestamp:
            return values[index][1]

        return "" if index == 0 else values[index-1][1]
        

        
