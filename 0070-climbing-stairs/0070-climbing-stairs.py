class Solution:
    def climbStairs(self, n: int) -> int:
        
        first, second = 0, 1
        res = 0
        for i in range(n):
            res = first + second
            first, second = second, res
        return res