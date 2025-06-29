class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def feasible(k):
            hr = 0
            for pile in piles:
                hr += pile // k
                if pile % k > 0:
                    hr += 1

            return hr <= h
        
        res = 0
        while left <= right:
            mid = (left + right)//2
            if feasible(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res