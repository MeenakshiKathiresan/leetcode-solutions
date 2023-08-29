class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0] * len(cost)
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i, c in enumerate(cost):
            if i <2:
                continue
            dp[i] = c + min(dp[i-1], dp[i-2])
            
        return min(dp[len(cost)-1], dp[len(cost)-2])