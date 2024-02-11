class Solution:
    def check(self, nums: List[int]) -> bool:
        outOfOrder = False
        highest = 0
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if not outOfOrder:
                    outOfOrder = True
                    return sorted(nums) == nums[i+1:] + nums[:i+1]
                else:
                    return False
        return True