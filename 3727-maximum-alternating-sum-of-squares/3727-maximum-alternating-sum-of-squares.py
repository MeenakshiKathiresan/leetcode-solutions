class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # greedy 
        nums.sort(key = lambda x: x * x)
        low = 0
        high = 0
        for i, num in enumerate(nums):
            if i < len(nums)//2:
                low += num * num
            else:
                high += num * num
                
        return high - low

        