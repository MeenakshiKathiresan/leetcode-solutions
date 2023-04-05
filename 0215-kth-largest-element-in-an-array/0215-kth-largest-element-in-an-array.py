import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        
        i = 0
        while i < k - 1:
            i+=1
            heapq._heappop_max(nums)
            
        return heapq._heappop_max(nums)