class Node:
    def __init__(self, val, key):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.first = Node(0, 0)
        self.last = Node(0, 0)
        self.first.next = self.last
        self.last.prev = self.first
        self.capacity = capacity

    def _move_to_front(self, node: Node):
        prev_mru = self.first.next
        self.first.next = node
        node.prev = self.first
        node.next = prev_mru
        prev_mru.prev = node
    
    def _remove(self, node: Node):
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._move_to_front(node)
            print(node.val)
            return node.val
        return - 1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) + 1 > self.capacity:
            lru = self.last.prev
            del self.cache[lru.key]
            self._remove(lru)

        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.val = value
        else:
            node = Node(value, key)
            self.cache[key] = node
        self._move_to_front(node)
        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)