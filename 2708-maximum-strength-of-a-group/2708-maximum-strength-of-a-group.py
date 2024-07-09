class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort it
        # remove 0
        # if even number of negative leave it
        # if odd number of negative, remove the smallest
        if (len(nums) == 1 and nums[0] == 0): return 0
         
        nums.sort()
        neg_count = 0
        largest_neg = 0
        i = 0
        while i < len(nums) and nums[i] < 0:
            neg_count += 1
            largest_neg = nums[i]
            i += 1
        
        if neg_count % 2 == 1 and len(nums) > 1 and (nums.index(largest_neg) != -1):
            nums[nums.index(largest_neg)] = 0
        
        all_zero = True
        for num in nums:
            if num != 0:
                all_zero = False
        
        if all_zero: return 0
        
        res = 1
            
        for num in nums:
            if num == 0: continue
            res *= num
            
        return res
            
            