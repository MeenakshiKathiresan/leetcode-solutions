class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [-1] * len(nums)
        def traverse(i):
            
            if i < 0:
                return 0
            if i == 0:
                return nums[i]
            if dp[i] != -1:
                return dp[i]
            
            take = nums[i] + traverse(i-2)
            not_take = traverse(i-1)
            
            dp[i] = max(take, not_take)
            return dp[i]
        
        return traverse(len(nums)-1)