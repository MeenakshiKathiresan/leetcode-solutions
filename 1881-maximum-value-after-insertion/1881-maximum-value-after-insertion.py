class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """

        # before the first number smaller than x, if none insert last
        
        # negative - before the first number greater than x, if none insert last
        
        # positive number
        if n[0] != '-':
            for i, digit in enumerate(n):
                if int(digit) < int(x):
                    return n[:i] + str(x) + n[i:]
            
            return n + str(x)
        
        else:
            for i, digit in enumerate(n[1:]):
                if int(digit) > int(x):
                    return n[:i+1] + str(x) + n[i+1:]
            
            return n + str(x)
        
        
        