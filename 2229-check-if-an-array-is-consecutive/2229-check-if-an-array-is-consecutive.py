class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        
        nums.sort()
        
        prev = nums[0] -1
        
        for num in nums:
            if num - 1 != prev:
                return False
            prev = num
        return True