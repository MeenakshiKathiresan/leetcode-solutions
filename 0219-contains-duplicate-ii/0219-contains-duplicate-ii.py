class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        no = {}
        for i, num in enumerate(nums):
            if num in no.keys():
                if abs(i - no[num]) <= k:
                    return True
                
            no[num] = i
        return False
                    