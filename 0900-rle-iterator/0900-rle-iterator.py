class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.RLE = {}
        self.RLE_queue = deque()
        

        for i in range(0,len(encoding), 2):
            if encoding[i] >0:
                self.RLE[(encoding[i+1],i)] = encoding[i] 
                self.RLE_queue.append((encoding[i+1], i))
        

    def next(self, n: int) -> int:
        last = -1
        
        
        while n > 0:
            if self.RLE_queue:
                if n <= self.RLE[self.RLE_queue[0]]:
                    self.RLE[self.RLE_queue[0]] -= n
                    last = self.RLE_queue[0][0]
                    n = 0
                else:
                    n -= self.RLE[self.RLE_queue[0]]
                    self.RLE_queue.popleft()
            else:
                last = -1
                break
            
        return last
            

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)