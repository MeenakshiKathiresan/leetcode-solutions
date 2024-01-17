import collections
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        nos = {}
        occur =set()
        
        nos = collections.Counter(arr)
            
        for v in nos.values():
            occur.add(v)
            
        return len(occur) == len(nos)