class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        block1 = 0
        block2 = 0
        
        max_sub = 0
        
        for i, num in enumerate(nums):
            if num == 1:
                block2 += 1
            elif num == 0:
                max_sub = max(max_sub, block1+block2)
                block1 = block2
                block2 = 0
                
                
        max_sub = max(max_sub, block1+block2)
        if max_sub == len(nums): return max_sub-1
        return max_sub
                