class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        # get index of max from left subarry
        
        start_val = max(nums[: len(nums)- k + 1])
        index = nums.index(start_val)
        
        return nums[index:index + k]