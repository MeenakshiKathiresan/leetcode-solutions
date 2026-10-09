class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # unique numbers - count
        zero = 0
        if 0 in nums:
            zero = 1
        return len(set(nums)) - zero
