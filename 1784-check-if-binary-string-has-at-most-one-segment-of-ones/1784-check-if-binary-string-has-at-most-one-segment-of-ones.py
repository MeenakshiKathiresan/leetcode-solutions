class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen_zero = False
        for ch in s:
            if ch == "0":
                seen_zero = True
            elif seen_zero:
                return False
        return True