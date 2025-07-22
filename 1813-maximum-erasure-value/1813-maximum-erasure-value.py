class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum = 0
        running_sum = 0
        left = 0
        seen = set()

        for right, num in enumerate(nums):
            while num in seen:
                running_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            running_sum += num
            seen.add(num)

            max_sum = max(max_sum, running_sum)

        return max_sum