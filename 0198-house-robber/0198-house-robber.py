class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        res = 0
        for i, n in enumerate(nums):
            rob = n + prev2
            
            no_rob = prev1
            res = max(rob, no_rob)
            prev2 = prev1
            prev1 = res
            
        
        return res