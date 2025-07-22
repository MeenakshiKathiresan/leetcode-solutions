class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique_elements = set()
        res = 0
        curr_sum = 0
        left = 0
        for right, num in enumerate(nums):
            # keep removing until this num is removed
            while num in unique_elements:
                curr_sum -= nums[left]
                unique_elements.remove(nums[left])
                left += 1
            curr_sum += num
            unique_elements.add(num)
            res = max(res, curr_sum)

        return res