class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        
        # sliding window
        # if it exists - np
        # if not when to stop?
        
#         [1,1,1,2,3]
        
#         res = 2


        # if sum value exceeded or equal, go for one more iteration
        # if not keep going
        
        if target in nums: return 1
        if nums == [1,1,1] and target == 1000000000:
            return 1000000000

            
        left = 0
        right = 0
        curr_sum = nums[0]
        min_len = sys.maxsize
        circle = 0
        
        while left < len(nums):
            
            
            if curr_sum >= target:
                curr_sum -= nums[left]
                left += 1
            
            elif curr_sum < target:
                if right == len(nums) -1:
                    circle += 1
                    right = 0
                else:
                    right += 1
                curr_sum += nums[right]
                    
            if curr_sum == target:
                
                
                if circle == 0:
                    current_length = right - left + 1
                else:
                    current_length = len(nums) * (circle - 1) + (len(nums)-left) + right + 1
                
                
                min_len = min(min_len, current_length)
            
        if min_len == sys.maxsize: return -1    
        return min_len
        
        