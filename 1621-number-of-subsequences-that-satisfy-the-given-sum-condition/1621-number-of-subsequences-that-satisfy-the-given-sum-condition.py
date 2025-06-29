class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        nums.sort()

        res = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                n = right - left
                res = (res + pow(2, n)) % mod
                left += 1

            else:
                right -= 1

            
        return res 


