class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        nums.sort()
        curr = original
        for num in nums:
            if num == curr:
                curr *= 2
        return curr