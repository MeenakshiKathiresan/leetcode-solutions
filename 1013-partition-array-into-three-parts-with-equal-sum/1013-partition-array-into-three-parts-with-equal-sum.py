class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr_sum = sum(arr)
        if arr_sum % 3 != 0: return False
        
        part = arr_sum/3
        
        
        count = 0
        curr_sum = 0
        
        for num in arr:
            curr_sum += num
            
            if curr_sum == part:
                count += 1
                curr_sum = 0
        
        return count >= 3