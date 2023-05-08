import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        target = len(nums)//3
        
        counter = Counter(nums)
        
        res = []
        
        for key, value in counter.items():
            if value > target:
                res.append(key)
                
        return res