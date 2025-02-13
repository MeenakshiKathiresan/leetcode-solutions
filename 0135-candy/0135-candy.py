class Solution:
    def candy(self, ratings: List[int]) -> int:
        # all valleys should be given 1
        # from valleys - travel 
                
        n = len(ratings)
        res = [1] * n
        
        # left to right
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        
        # right to left
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1] + 1)
                
        return sum(res)