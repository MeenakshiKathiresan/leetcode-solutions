class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0 
        right = len(nums) - 1
        res = -1
        """
        when mid is higher than left => smallest in the left or right
        when mid is smaller than left => 
        
        """
        while left < right:
            mid = (left + right)//2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 


        return nums[left]
            