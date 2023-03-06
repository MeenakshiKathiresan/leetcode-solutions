class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0 , len(arr)-1
        
        while l <= r:
            m = (l+r)//2
            
            if arr[m] - (m+1) < k:
                l = m + 1
            else:
                r = m -1 
            
        return l + k
      
            
            
        
        