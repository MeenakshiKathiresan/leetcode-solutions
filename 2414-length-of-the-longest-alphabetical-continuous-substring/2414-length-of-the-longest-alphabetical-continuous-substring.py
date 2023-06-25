class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        prev = None
        longest = 0
        current = 0
        
        for ch in s:
            if prev != None and ord(ch) - ord(prev) == 1:
                current += 1
            else:
                longest = max(current+1, longest)
                current = 0
            prev = ch
        longest = max(current+1, longest)
        return longest
            