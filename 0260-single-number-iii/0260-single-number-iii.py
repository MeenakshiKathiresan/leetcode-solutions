class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        occurred = set()
        
        for num in nums:
            if num not in occurred:
                occurred.add(num)
            else:
                occurred.remove(num)
        
        return list(occurred)