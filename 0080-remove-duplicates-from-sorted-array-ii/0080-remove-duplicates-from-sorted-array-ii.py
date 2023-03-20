class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        count = 0
        
        if len(nums) < 3: return len(nums)
        
        while j < len(nums):
            
            if j < len(nums) - 2: 
                if not (nums[j] == nums[j+1] == nums[j+2]):
                    nums[i] = nums[j]
                    i += 1
                else:
                    count += 1
            
            j += 1
            
        
        nums[i] = nums[j-2]
        nums[i+1] = nums[j-1]
        return len(nums)-count