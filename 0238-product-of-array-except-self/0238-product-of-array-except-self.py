class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prefix = 1
        postfix = 1

        res = []

        # left to right
        for i, n in enumerate(nums):
            if i == 0:
                res.append(1)
            else:
                prefix *= nums[i-1]
                res.append(prefix)
        
        # right to left 
        for i in range(len(nums) - 2, -1, -1):
            postfix *= nums[i+1]
            res[i] *= postfix
        
        return res

                