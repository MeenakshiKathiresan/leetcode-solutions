class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
       
        res = 0
        min_pos = max_pos = left = -1
        
        for i, num in enumerate(nums):
            if num > maxK or num < minK:
                left = i
                
            if num == minK: 
                min_pos = i
            if num == maxK: 
                max_pos = i
        
            res += max(0, min(min_pos, max_pos) - left)
            
        return res