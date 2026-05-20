class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = deque([])
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.lru.remove(key)
        self.lru.appendleft(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # overflow is not possible
            self.cache[key] = value
            self.lru.remove(key)
            self.lru.appendleft(key)
        else:
            if len(self.cache) >= self.capacity:
                last = self.lru.pop()
                del self.cache[last]
            self.cache[key] = value
            self.lru.appendleft(key)
        
