class TimeMap:
    # dictionary with value dictionary

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        values = self.time_map[key]
        left = 0
        right = len(values) - 1
        match = -1

        while left <= right:
            mid = (left + right)// 2

            if values[mid][0] > timestamp:
                right = mid - 1
            else:
                match = mid
                left = mid + 1
                
        
        if match == -1: return ""
        return values[match][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)