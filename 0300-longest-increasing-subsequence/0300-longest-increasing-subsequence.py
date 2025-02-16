class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]

        for i, n in enumerate(nums):
            for j, p in enumerate(nums[:i]):
                if n > p:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        