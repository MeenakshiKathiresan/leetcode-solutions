class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort_nums = sorted(nums)
        
        nums_dict = {}
        
        for i, num in enumerate(sort_nums):
            if num not in nums_dict:
                nums_dict[num] = i
        
        res = []
        for num in nums:
            res.append(nums_dict[num])
            
        return res