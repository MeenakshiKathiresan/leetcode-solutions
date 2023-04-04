class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        max_score = -100000
        
        current = 0
        for num in nums:
            current += num
            max_score = max(current, max_score)
            
        current = 0
        for i in range(len(nums) -1, -1, -1):
            current += nums[i]
            max_score = max(current, max_score)
            
        return max_score