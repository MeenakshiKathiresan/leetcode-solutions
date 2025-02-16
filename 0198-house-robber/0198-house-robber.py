class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]

        for i, n in enumerate(nums):
            rob = n 

            if i > 1:
                rob += dp[i - 2]
            
            no_rob = dp[i-1]
            dp[i] = max(rob, no_rob)
        
        return dp[-1]