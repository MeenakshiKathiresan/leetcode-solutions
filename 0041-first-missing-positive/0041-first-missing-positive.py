class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numbers = set()
        
        for i in range(len(nums)+1):
            numbers.add(i+1)
            
        for num in nums:
            if num in numbers:
                numbers.remove(num)
                
        return list(numbers)[0]