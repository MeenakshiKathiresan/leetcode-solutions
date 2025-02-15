class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            curr_sum = -float('inf')
            max_sum = curr_sum
            for num in nums:
                curr_sum = max(num + curr_sum, num)
                max_sum = max(max_sum, curr_sum)
            return max_sum
        max_kadane = kadane(nums)
        min_kadane = -kadane([-num for num in nums])

        total = sum(nums)
        if min_kadane == total: 
            return max_kadane
        return max(max_kadane, total - min_kadane)