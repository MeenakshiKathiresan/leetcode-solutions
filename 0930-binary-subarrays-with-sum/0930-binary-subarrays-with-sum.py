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
        subarray_count = {0: 1} 
        
        for num in nums:
            current_sum += num
            
            if current_sum >= goal:
                count += subarray_count.get(current_sum - goal, 0)
            
            subarray_count[current_sum] = subarray_count.get(current_sum, 0) + 1
        
        return count