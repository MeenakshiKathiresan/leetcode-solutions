class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ranking = {}

        rank = 1
        for num in sorted(list(arr)):
            if num not in ranking:
                ranking[num] = rank
                rank += 1
        
        res = []
        for num in arr:
            res.append(ranking[num])

        return res