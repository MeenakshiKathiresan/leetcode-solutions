class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        remaining = sum(nums)
        current = 0
        res = 0
        for num in nums[:-1]:
            current += num
            remaining -= num
            
            if abs(current - remaining) % 2 == 0:
                res += 1
        return res