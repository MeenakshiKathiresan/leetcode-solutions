class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key = lambda x:x[1])
        curr_car = 0
        heap = []
        
        for i, trip in enumerate(trips):
            while len(heap) > 0 and heap[0][0] <= trip[1]:
                    curr_car -= heap[0][1]
                    heapq.heappop(heap)
            if curr_car + trip[0] <= capacity:
                curr_car += trip[0]
                heapq.heappush(heap, [trip[2],trip[0]])
            else:
                return False
        return True
            