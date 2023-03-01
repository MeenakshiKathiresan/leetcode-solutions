class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # binary search through 1 to max val of piles
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            mid = l + (r-l)/2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(float(pile)/float(mid))
            if hrs <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
            
        return res
                
                