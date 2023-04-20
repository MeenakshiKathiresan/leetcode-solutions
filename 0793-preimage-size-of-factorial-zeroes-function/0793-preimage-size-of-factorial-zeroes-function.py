class Solution(object):
    def countZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count
    
    def preimageSizeFZF(self, k):
        """
        :type k: int
        :rtype: int
        """
        lo, hi = 0, 2**32-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.countZeroes(mid) < k:
                lo = mid + 1
            elif self.countZeroes(mid) > k:
                hi = mid - 1
            else:
                return 5
        return 0