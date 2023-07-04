class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        chunk_max = 0
        chunk_count = 0
        
        for i, num in enumerate(arr):
            if num > chunk_max:
                chunk_max = num
            else:
                if i == chunk_max:
                    chunk_count+=1
                    chunk_max+=1
                    
        return chunk_count