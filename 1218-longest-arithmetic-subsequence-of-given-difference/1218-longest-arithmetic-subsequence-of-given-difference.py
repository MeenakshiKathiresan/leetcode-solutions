class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        
        for n in arr:
            dp[n] = 0
            
        for n in arr:
            prev = 0
            if n-difference in dp:
                prev = dp[n-difference]
            
            dp[n] = prev + 1
            
        return max(dp.values())