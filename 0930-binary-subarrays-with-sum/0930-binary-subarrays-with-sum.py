class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        
        left = 0
        current_sum = 0
        count = 0
        res = 0
        
        for i, num in enumerate(nums):
            
            current_sum += num
            
            if num == 1:
                count = 0
            
            while current_sum >= goal and left <= i:

                    if current_sum == goal:
                        count += 1
                    
                    current_sum -= nums[left]
                    left += 1
            res+= count
        

        return res
        
    