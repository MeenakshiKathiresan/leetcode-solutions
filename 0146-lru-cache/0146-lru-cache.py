class LRUCache:

    def __init__(self, capacity: int):
        self.kvp = {}
        self.kvp_access = []
        self.capacity = capacity
        
        

    def get(self, key: int) -> int:
        # update access
        
        if key in self.kvp:
        
            # find that value - pop and append
            recently_used = self.kvp_access.pop(self.kvp_access.index(key))
            self.kvp_access.append(recently_used)
            return self.kvp[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.kvp:
            recently_used = self.kvp_access.pop(self.kvp_access.index(key))
            self.kvp_access.append(recently_used)
            self.kvp[key] = value
            
        elif len(self.kvp) < self.capacity :
            self.kvp[key] = value
            self.kvp_access.append(key)
            
        else:
            # remove the least used
            self.kvp.pop(self.kvp_access[0])
            self.kvp_access.pop(0)
            self.kvp[key] = value
            
            self.kvp_access.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)