from collections import deque
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.usage_frequency = deque([])
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move key to front of usage queue
        if key in self.usage_frequency:
            self.usage_frequency.remove(key)
        self.add(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # Update cache
        self.cache[key] = value
        # Update LRU order: remove key if it exists, then add to front
        if key in self.usage_frequency:
            self.usage_frequency.remove(key)
        self.add(key)
        # Evict if over capacity
        if len(self.cache) > self.capacity:
            removed = self.usage_frequency.pop()
            if removed in self.cache:  # Ensure key exists in cache
                del self.cache[removed]

    def remove(self, key: int = -1) -> int:
        if key == -1 and self.usage_frequency:
            return self.usage_frequency.pop()
        if key in self.usage_frequency:
            self.usage_frequency.remove(key)
            return key
        return -1

    def add(self, key: int) -> None:
        self.usage_frequency.appendleft(key)