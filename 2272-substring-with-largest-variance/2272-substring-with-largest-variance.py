import collections

class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        chars = set(s)
        max_variance = 0
        for c1, c2 in itertools.product(chars, chars):
            if c1 == c2:
                continue
            diff = min_diff = last_diff = 0 
            met1 = met2 = False
            for i, c in enumerate(s):
                if c == c1:
                    met1 = True
                    diff += 1
                elif c == c2:
                    met2 = True
                    diff -= 1
                    last_diff = min_diff
                    min_diff = min(min_diff, diff)
                else:
                    continue
                if met1 and met2:
                    max_variance = max(max_variance, diff - last_diff)
        return max_variance