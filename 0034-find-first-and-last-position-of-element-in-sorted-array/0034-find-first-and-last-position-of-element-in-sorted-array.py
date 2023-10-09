class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        
        ans = [-1,-1]
        mid = 0
        if len(nums) < 1: return ans
        
        while start <= end:
            mid = (start + end)//2
            
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                ans[0] = mid 
        
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
                ans[1] = mid
        if ans[0] > ans[1] or ans[0] < 0 or ans[1] < 0 or ans[1] >= len(nums) or ans[0] >= len(nums): return [-1,-1]
        return ans