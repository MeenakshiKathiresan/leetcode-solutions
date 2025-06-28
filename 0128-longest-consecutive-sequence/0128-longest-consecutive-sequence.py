class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        nums.sort()
        res = 1
        curr = 1
        print(nums)
        for i, num in enumerate(nums):
            if i > 0:
                if num == nums[i - 1]:
                    continue
                if num == nums[i-1] + 1:
                    print(curr)
                    curr += 1
                else:
                    print(num, i, "reset ")
                    curr = 1
            res = max(res, curr)
        
        return res