class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        if len(nums) == 1:
            return [[nums[0]]]

        for i in range(len(nums)):
            n = nums.pop()
            perms = self.permute(nums)

            for perm in perms:
                perm.insert(0, n)
            result.extend(perms)
            nums.insert(0,n)
        
        return result

