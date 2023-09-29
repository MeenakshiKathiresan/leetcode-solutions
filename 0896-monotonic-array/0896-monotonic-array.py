class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = 0
        
        for i, num in enumerate(nums[:-1]):
            if increasing == 0:
               
                if nums[i] > nums[i+1]:
                    increasing = -1
                elif nums[i] < nums[i+1]:
                    increasing = 1
            else:
                if (nums[i] < nums[i+1] and increasing == -1) or (nums[i] > nums[i+1] and increasing == 1):
                    return False
        return True
    