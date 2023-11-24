class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        
        for i, pile in enumerate(piles[:len(piles)//3]):
            res += piles[-(2*(i+1))]
        return res
            
            