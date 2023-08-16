class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total_len = len(nums) 
        nums = sorted(set(nums))  
        n = len(nums)
        l, r = 0, 0
        max_window = 1
        
        while r < n:
            if nums[r] - nums[l] < total_len:
                r += 1
            else:
                l += 1
            max_window = max(max_window, r - l)
        return total_len - max_window