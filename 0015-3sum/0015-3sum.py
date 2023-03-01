class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # [-4, -1, -1, 0, 1, 2] 
        #
        
        # sort array
        # left right pointer and look for a number
        # make it to set?
        
        nums.sort()
        ans = []
        
        for i, n in enumerate(nums):
            
            # avoid repeats
            if i>0 and n == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums) - 1
            
            while left < right:
                num = nums[i] + nums[left] + nums[right]
                
                if num > 0:
                    right -= 1
                elif num < 0:
                    left += 1
                else:
                    # found a match
                    ans.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return ans
                
        
        