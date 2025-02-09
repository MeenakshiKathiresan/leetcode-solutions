class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # subtract its position from its value
        # count the number of same value
        # (n * n - 1 / 2) - (same values)

        def combo(n):
            return (n * (n-1)) / 2 

        for i, n in enumerate(nums):
            nums[i] -= i
        
        res = combo(len(nums))

        for k, v in Counter(nums).items():
            if v > 1:
                res -= combo(v)

        return int(res)
