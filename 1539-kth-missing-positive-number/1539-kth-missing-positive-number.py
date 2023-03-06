class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        nums = []
        count = 1
        i =0
        while i< len(arr):
            num = arr[i]
            if num != count:
                nums.append(count)
                
                if len(nums) == k:
                    return nums[-1]
            else:
                
                
                i+=1
                
            count+=1
            
        return arr[-1] + k - len(nums)
      
            
            
        
        