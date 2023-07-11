class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = collections.Counter(nums)
        res = []
        for k, v in freq.items():
            if v == 2:
                res.append(k)
        return res