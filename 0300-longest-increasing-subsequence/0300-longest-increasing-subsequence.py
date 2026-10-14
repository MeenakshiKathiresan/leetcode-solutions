class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = [1 for i in nums] 
        for i, num in enumerate(nums):
            for j, num_comp in enumerate(nums[:i]):
                if num_comp < num:
                    lis[i] = max(lis[i], lis[j] + 1)

        return max(lis)
