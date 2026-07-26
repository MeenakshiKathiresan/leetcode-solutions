class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if all positive - pick highest 3
        # if 2 negative, pick that and highest
        # if 3 - take all 3

        nums.sort()

        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        
        neg = nums[0] * nums[1] * nums[-1]
        pos = nums[-1] * nums[-2] * nums[-3]
        return max(neg, pos)