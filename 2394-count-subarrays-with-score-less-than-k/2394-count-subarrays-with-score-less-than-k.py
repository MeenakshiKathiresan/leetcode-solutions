class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        
        curr_sum = 0
        curr_len = 0
        res = 0
        while right < len(nums):          
            
            curr_sum += nums[right]
            curr_len += 1

            while left <= right and  curr_sum * curr_len >= k:
                curr_sum -= nums[left]
                curr_len -= 1                 
                left += 1

            right += 1
            res += right - left

        return res