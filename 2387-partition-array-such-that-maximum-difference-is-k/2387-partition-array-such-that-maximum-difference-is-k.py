class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0 # store start index of the range
        res = 1
        for i, num in enumerate(nums):
            if num - nums[start] > k:
                res += 1
                start = i

        return res
            