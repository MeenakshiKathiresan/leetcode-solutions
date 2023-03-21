class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        zero_counter = 0
        res = 0
      
        
        for num in nums:
            if num == 0:
                zero_counter += 1
            else:
                zero_counter = 0
            res += zero_counter
            
        return res