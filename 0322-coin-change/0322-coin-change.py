class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def recurse(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in dp:
                return dp[amount]

            res = float('inf')
            min_res = float('inf')
            for c in coins:
                if amount >= c:
                    res = recurse(amount  - c)
                    min_res = min(res + 1, min_res)
            dp[amount] = min_res
            return min_res
            
        res = recurse(amount) 
        if res == float('inf'): return -1
        return res
                
                

            
            