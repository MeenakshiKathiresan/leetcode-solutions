class LRUCache:

    def __init__(self, capacity: int):
        self.keys = {}
        self.cache = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.keys:
            self.cache.remove(key)
            self.cache.appendleft(key)
            return self.keys[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.keys and self.capacity - len(self.keys) < 1:
            lru = self.cache.pop()
            del self.keys[lru]
        
        self.keys[key] = value
        if key in self.cache:
            self.cache.remove(key)
        self.cache.appendleft(key)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)