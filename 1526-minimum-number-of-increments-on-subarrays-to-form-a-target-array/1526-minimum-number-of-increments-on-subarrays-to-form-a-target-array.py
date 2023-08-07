class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        res = 0
        prev = 0
        
        for current in target:
            res += max(current - prev, 0)
            prev = current
            
        return res