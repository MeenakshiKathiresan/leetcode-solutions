import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        counter = collections.Counter(s)
        res = ""
        for letter in sorted(counter, key = lambda x:counter[x], reverse=True):
            res+=(letter * counter[letter])
        return res