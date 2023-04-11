class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # traverse in reverse
        # count star
        # slice out
        
        i = 0
        star_count = 0
        while i < len(s):
            if s[i]!= '*':
                if star_count > 0:
                    s = s[:i-(star_count*2)] + s[i:]
                    i -= (star_count*2)
                star_count = 0
            else:
                star_count += 1
            i+= 1
        if star_count > 0:
            s = s[:i-(star_count*2)] + s[i:]
        return s
            