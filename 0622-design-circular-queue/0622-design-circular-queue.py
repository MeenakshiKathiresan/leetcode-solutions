class MyCircularQueue:
    

    def __init__(self, k: int):
        self.my_queue = []
        self.size = k
        self.curr = 0

    def enQueue(self, value: int) -> bool:
        if self.curr < self.size:
            self.my_queue.append(value)
            self.curr+=1
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        
     
        if len(self.my_queue)>0:
            self.my_queue.pop(0)
            self.curr-=1
            return True
        else:
            return False
        

    def Front(self) -> int:
        if len(self.my_queue) > 0:
            return self.my_queue[0]
        return -1
        

    def Rear(self) -> int:
        if len(self.my_queue) > 0:
                return self.my_queue[-1]
        return -1
        

    def isEmpty(self) -> bool:
        return len(self.my_queue) == 0

    def isFull(self) -> bool:
        return len(self.my_queue) == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()