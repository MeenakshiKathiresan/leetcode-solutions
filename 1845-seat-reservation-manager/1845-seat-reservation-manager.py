import heapq
class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        self.pointer = 1
        

    def reserve(self) -> int:
        if self.heap:
            return heappop(self.heap)
        self.pointer += 1
        return self.pointer - 1
        

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)