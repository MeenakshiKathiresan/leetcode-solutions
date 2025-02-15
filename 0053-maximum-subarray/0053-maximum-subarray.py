class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = -float('inf')
        max_sum = curr_sum
        for num in nums:
            curr_sum = max(num + curr_sum, num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
