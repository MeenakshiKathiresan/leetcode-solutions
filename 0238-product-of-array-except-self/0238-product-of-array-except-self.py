class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # iterate from left to right to store prefix of each
        prefix = postfix = 1
        
        ans = []
        
        for i, num in enumerate(nums):
            if i == 0:
                ans.append(1)
            else:
                prefix *= nums[i-1]
                ans.append(prefix)
        
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                
                postfix *= nums[-i]
                ans[-i-1] *= postfix
        return ans
                
            
            