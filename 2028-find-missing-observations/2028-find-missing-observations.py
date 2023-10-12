class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        # count = len(rolls) + n 
            # sum/count = avg
        # sum = avg * count
        # sum of rolls + n(x) = mean * count
        # n * x = (mean * count) - sum
        
        # x = ((mean * count) - sum) /n
        
        # count = 7
        
        # 3 * 7 = 21 -> total
        # 12 + 4(x) = 21
        # 4x = 9
        # x = 2.25
        ans = []
        
        count = len(rolls) + n
        appx_sum = mean * count
        x = (appx_sum - sum(rolls))
        return [x / n + (i < x % n)  for i in xrange(n)] if n <= x <= n * 6 else []
        
        