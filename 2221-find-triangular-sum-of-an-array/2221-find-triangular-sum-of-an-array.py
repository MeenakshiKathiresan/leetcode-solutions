class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        while len(nums)>1:
            for i, num in enumerate(nums[:-1]):
                nums[i] = (nums[i]+nums[i+1]) % 10

            nums.pop()
        
        return nums[0]